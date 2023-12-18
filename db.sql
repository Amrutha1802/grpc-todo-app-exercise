--creation queries

--create a data base 
sqlite3 todo.db

--Table todo
CREATE TABLE todos (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT,
    status INTEGER
);


