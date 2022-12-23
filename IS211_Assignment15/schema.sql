CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author TEXT NOT NULL,
  heading TEXT NOT NULL,
  content TEXT NOT NULL,
  timestamp DATETIME NOT NULL
);


/*
The schema.sql file should contain the SQL statements needed to create the database schema for the application. 
This could include statements to create tables, indices, and any other database objects needed by the application.
*/

/*
This creates a posts table with columns for the id, author, heading, content, and timestamp of each post. 
The id column is set as the primary key and the other columns are defined as not null to ensure that they contain valid values. 
You can add additional columns or tables as needed by the application.
Note that the schema.sql file should only contain the SQL statements needed to create the schema, not any data manipulation statements. 
Data manipulation statements (such as INSERT or UPDATE) should be handled by the application code.
*/