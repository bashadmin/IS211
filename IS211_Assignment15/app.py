import sqlite3
from datetime import datetime
from typing import List, Tuple
from flask import Flask, session, url_for, escape, render_template, request, redirect

db = sqlite3.connect("final.db")
c = db.cursor()

setup = open('schema.sql', 'r').read()
c.executescript(setup)
db.commit()


app = Flask(__name__)

# Use a database-agnostic API to make it easier to switch between different database systems
def get_db() -> sqlite3.Connection:
    return sqlite3.connect("final.db")

def init_db() -> None:
    with get_db() as db:
        with open('schema.sql', 'r') as f:
            schema = f.read()
        db.executescript(schema)

# Use functions to extract complex or repetitive logic
def render_login(message: str = "You are not logged in") -> str:
    return render_template("login.html", message=message)

def check_session() -> bool:
    return "username" in session

# http://flask.pocoo.org/docs/0.10/quickstart/#sessions
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("dashboard"))
    if check_session():
        return redirect("/dashboard")
    else:
        return render_login()

@app.route("/")
def index() -> str:
    with get_db() as db:
        c = db.cursor()
        c.execute("SELECT * FROM posts ORDER BY timestamp DESC")
        posts = c.fetchall()
    return render_template("index.html", posts=posts)

@app.route("/dashboard")
def dashboard() -> str:
    if check_session():
        with get_db() as db:
            c = db.cursor()
            c.execute("SELECT * FROM posts WHERE author = ?", [session["username"]])
            posts = c.fetchall()
        return render_template("dashboard.html", posts=posts)
    else:
        return render_login()

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
