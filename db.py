import sqlite3


class TodoDB:
    def __init__(self, db_file="todo.db"):
        self.db_conn = sqlite3.connect(db_file, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        try:
            with self.db_conn as db_conn:
                cursor = db_conn.cursor()
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS todo_items (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        status TEXT
                    )
                    """
                )
        except sqlite3.Error as e:
            raise e
