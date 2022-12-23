import sqlite3
import datetime as dt
from flask import Flask, session, url_for, escape, render_template, request, redirect

# Use an ORM to abstract away the underlying database and simplify database operations
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Use a configuration file to store sensitive information
app.config.from_pyfile('config.cfg')

# Set up the database connection
Base = declarative_base()
engine = create_engine(app.config['DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

# Define the Post model
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    author = Column(String)
    heading = Column(String)
    content = Column(Text)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f'<Post(author={self.author}, heading={self.heading}, content={self.content}, timestamp={self.timestamp})>'

# Create the database schema
Base.metadata.create_all(engine)

# Define a function to render the login page and check the user's session
def render_login_page(message=None):
    if 'username' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', message=message or 'You are not logged in')

# Define a function to retrieve all posts from the database
def get_posts():
    # Use parameterized queries to prevent SQL injection attacks
    query = session.query(Post).order_by(Post.timestamp.desc())
    return query.all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))
    return render_login_page()

@app.route('/')
def index():
    # Call the function to retrieve all posts from the database
    posts = get_posts()
    return render_template('index.html', posts=posts)

@app.route('/dashboard')
def dashboard():
    # Check the user's session and call the function to retrieve their posts from the database
    if 'username' in session:
        # Use parameterized queries to prevent SQL injection attacks
        query = session.query(Post).filter(Post.author == session['username'])
        posts = query.all()
        return render_template('dashboard.html', posts=posts)
    else:
        return render_login_page()

@app.route("/add-story", methods=["POST"])
def add_story() -> str:
    with get_db() as db:
        c = db.cursor()
        c.execute(
            "INSERT INTO posts (author, heading, content, timestamp) VALUES (?, ?, ?, ?)",
            [session["username"], request.form["title"], request.form["content"], datetime.now()],
        )
        db.commit()
    return redirect(url_for("dashboard"))

@app.route("/edit-story", methods=["POST"])
def edit_story() -> str:
    with get_db() as db:
        c = db.cursor()
        c.execute(
            "UPDATE posts SET heading=?, content=? WHERE id=?",
            [request.form["title"], request.form["content"], request.form["id"]],
        )
        db.commit()
    return redirect(url_for("dashboard"))

    @app.route("/delete/<int:id>", methods=["GET"])
def delete(id: int) -> str:
    with get_db() as db:
        c = db.cursor()
        c.execute("DELETE FROM posts WHERE id=?", [id])
        db.commit()
    return redirect(url_for("dashboard"))

@app.route("/edit/<int:id>", methods=["GET"])
def edit(id: int) -> str:
    if check_session():
        with get_db() as db:
            c = db.cursor()
            c.execute("SELECT * FROM posts WHERE id = ?", [id])
            post = c.fetchone()
        return render_template("edit.html", post=post)
    else:
        return render_login()

@app.route("/logout")
def logout() -> str:
    # remove the username from the session if it's there
    session.pop("username", None)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.secret_key = "secret"
    app.run()
