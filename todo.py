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
                sql = "SELECT title,status from todo_items where id=?"
                val = (inserted_id,)
                cursor.execute(sql, val)
                todo = cursor.fetchone()
                return todo_pb2.Todo(id=inserted_id, title=todo[0], status=todo[1])
        except:
            raise

    def list_all_todos(self, request):
        try:
            with self.db_conn as db_conn:
                cursor = db_conn.cursor()
                cursor.execute("SELECT id, title, status FROM todo_items")
                rows = cursor.fetchall()
                todos_list = [
                    {"id": row[0], "title": row[1], "status": row[2]} for row in rows
                ]
            return todo_pb2.ListAllTodosResponse(todos=todos_list)
        except:
            raise
