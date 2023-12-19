--creation queries

--create a data base 
sqlite3 todo.db

--Table todo
CREATE TABLE todo_items (
    id INTEGER PRIMARY KEY,
    title TEXT,
    status TEXT
);


