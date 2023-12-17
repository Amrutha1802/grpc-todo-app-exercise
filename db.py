import sqlite3


class TodoDB:
    def __init__(self, db_file="todo.db"):
        self.db_file = db_file
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_file) as db_conn:
            cursor = db_conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS todo_items (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    status INTEGER
                )
                """
            )

    def add_todo(self, title, status):
        try:
            with sqlite3.connect(self.db_file) as db_conn:
                sql = "insert into todo_items(title,status) values(?,?) "
                val = (title, status)
                cursor = db_conn.cursor()
                cursor.execute(sql, val)
                db_conn.commit()
        except sqlite3.Error as e:
            raise e

    def list_all_todos(self):
        try:
            with sqlite3.connect(self.db_file) as db_conn:
                cursor = db_conn.cursor()
                cursor.execute("SELECT id, title, status FROM todo_items")
                rows = cursor.fetchall()
                todos = [
                    {"id": row[0], "title": row[1], "status": row[2]} for row in rows
                ]
                return todos
        except sqlite3.Error as e:
            raise e
