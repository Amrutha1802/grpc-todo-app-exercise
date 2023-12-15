--creation queries

--create a data base 
sqlite3 todo.db

--Table todo
CREATE TABLE todo_items (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT,
    status INTEGER
);


