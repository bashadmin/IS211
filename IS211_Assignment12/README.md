# IS211_Assignment12
IS211_Assignment12

Last week we started learning about Flask, a web development framework in Python. We reviewed the basic concepts that underlie what a framework does, and built a small example of how it all fits together.  This week, we will expand on that, digging a little deeper into Models and how we can integrate a relational databases into our web applications. We will continue to use SQLite as our database backend. We will also learn some techniques to help debug your Flask applications, which could come in handy when working on your class project. First, we will take a quick detour and talk about sessions.
Here are some patterns on how to use sqlite and flask
https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
https://pythonbasics.org/flask-sqlite/
A longer tutorial:
https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-and-sqlite

This week, which is our last week for web development, we reviewed how we can extend our Flask applications to use a relational database (SQLite). In this vein, you will develop a small application in Flask. The purpose of this application is to keep track of students that are enrolled in a class, and the score they have received on quizzes in the class. You will have to import a database model in a SQLite database, and use this database to allow a teacher to:
Add students, add quizzes and to add quiz results to the database
View the current list of students, quizzes and the student’s quiz results
