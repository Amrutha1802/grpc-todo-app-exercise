--creation queries

--create a data base 
sqlite3 todo.db

--Table todo_lists
CREATE TABLE todos (
    id INTEGER PRIMARY KEY,
    title TEXT,
    status INTEGER
);


