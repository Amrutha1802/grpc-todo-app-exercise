import sqlite3

import todo_app_pb2 as pb2


class TodoDB:
    def __init__(self):
        self.db_conn = sqlite3.connect("todo.db", check_same_thread=False)

    def get_users(self):
        try:
            with self.db_conn as db_conn:
                cursor = db_conn.cursor()
                sql = "SELECT id,name FROM users"
                cursor.execute(sql)
                result = cursor.fetchall()
                users_list = []
                for row in result:
                    user = {
                        "id": row[0],
                        "name": row[1],
                    }
                    users_list.append(user)
                return pb2.UsersList(users=users_list)
        except:
            raise

    def _check_for_user(self, id):
        try:
            with self.db_conn as db_conn:
                cursor = db_conn.cursor()
                sql = "SELECT 1 FROM users WHERE id=?"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
                if result:
                    return True
                else:
                    return False
        except:
            raise

    def _check_for_todo(self, id):
        try:
            with self.db_conn as db_conn:
                cursor = db_conn.cursor()
                sql = "SELECT 1 FROM todos WHERE id=?"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
                if result:
                    return True
                else:
                    return False
        except:
            raise

    def add_user(self, request):
        try:
            if len(request.name) == 0:
                raise Exception("Name cannot be empty")
            with self.db_conn as db_conn:
                sql = "INSERT INTO users(name) VALUES (?)"
                cursor = db_conn.cursor()
                cursor.execute(sql, (request.name,))
                inserted_id = cursor.lastrowid
                sql = "SELECT * FROM users WHERE id=?"
                cursor.execute(sql, (inserted_id,))
                user = cursor.fetchone()
                return pb2.User(id=user[0], name=user[1])
        except Exception as e:
            raise e

    def add_todo(self, request):
        try:
            if len(request.title) == 0:
                raise Exception("Title cannot be empty")
            user_exists = self._check_for_user(request.user_id)
            if not user_exists:
                raise Exception("User with given user_id donot exist")
            with self.db_conn as db_conn:
                sql = "INSERT INTO todos(title,user_id,status) VALUES(?,?,?) "
                val = (request.title, request.user_id, pb2.Status.Name(pb2.INCOMPLETE))
                cursor = db_conn.cursor()
                cursor.execute(sql, val)
                inserted_id = (cursor.lastrowid,)
                sql = "SELECT * FROM todos WHERE id=?"
                cursor.execute(sql, inserted_id)
                todo = cursor.fetchone()
                return pb2.Todo(
                    id=todo[0],
                    user_id=todo[1],
                    title=todo[2],
                    status=todo[3],
                )
        except:
            raise

    def get_user_todos(self, request):
        try:
            user_exists = self._check_for_user(request.id)
            if not user_exists:
                raise Exception("User with given user id donot exist")
            with self.db_conn as db_conn:
                cursor = db_conn.cursor()
                sql = "SELECT id,user_id,title,status FROM todos WHERE user_id=?"
                val = (request.id,)
                cursor.execute(sql, val)
                result = cursor.fetchall()
                todos_list = []
                for row in result:
                    dict = {
                        "id": row[0],
                        "user_id": row[1],
                        "title": row[2],
                        "status": row[3],
                    }
                    todos_list.append(dict)
                return pb2.UserTodos(todos=todos_list)
        except:
            raise

    def edit_todo(self, request):
        try:
            if not request.id:
                raise Exception("id cannot be empty")
            if not self._check_for_todo(request.id):
                raise Exception(
                    f"Todo with an id {request.id} donot exist, so it cannot be edited"
                )
            with self.db_conn as db_conn:
                cursor = db_conn.cursor()
                sql = "UPDATE todos SET"
                val = []
                if request.title:
                    sql += " title=?,"
                    val.append(request.title)
                if request.status:
                    sql += " status=?,"
                    val.append(pb2.Status.Name(request.status))
                sql = sql.rstrip(",")
                sql += " WHERE id=? "
                val.extend([request.id])
                print(val)
                if len(val) == 1:
                    raise Exception("Title or status is required to edit a todo")
                cursor.execute(sql, val)
                sql = "SELECT id,user_id,title,status FROM todos WHERE id=?"
                val = (request.id,)
                cursor.execute(sql, val)
                row = cursor.fetchone()
                todo = {
                    "id": row[0],
                    "user_id": row[1],
                    "title": row[2],
                    "status": row[3],
                }
            return pb2.Todo(
                id=todo["id"],
                user_id=todo["user_id"],
                title=todo["title"],
                status=todo["status"],
            )
        except:
            raise

    def delete_todo(self, request):
        try:
            if not self._check_for_todo(request.id):
                raise Exception(
                    f"Todo with an id {request.id} donot exist, so it cannot be deleted"
                )
            with self.db_conn as db_conn:
                if not self._check_for_todo(request.id):
                    raise Exception(
                        f"Todo with an id {request.id} donot exist, so it cannot be deleted"
                    )
                cursor = db_conn.cursor()
                sql = "DELETE FROM todos WHERE id = ? "
                val = (request.id,)
                cursor.execute(sql, val)
                print("Todo item removed")
                return pb2.EmptyResponse()
        except:
            raise
