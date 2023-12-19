import sqlite3

import todo_app_pb2 as todo_pb2


class Todo:
    def __init__(self):
        self.db_conn = sqlite3.connect("todo.db", check_same_thread=False)

    def add_todo(self, request):
        try:
            title = request.title
            if len(request.title) == 0:
                raise Exception("Title cannot be empty")
            with self.db_conn as db_conn:
                sql = "INSERT INTO todo_items(title, status) VALUES(?,?) "
                status = todo_pb2.Status.Name(todo_pb2.INCOMPLETE)
                val = (title, status)
                cursor = db_conn.cursor()
                cursor.execute(sql, val)
                inserted_id = cursor.lastrowid
                return todo_pb2.Todo(id=inserted_id, title=title, status=status)
        except:
            raise


