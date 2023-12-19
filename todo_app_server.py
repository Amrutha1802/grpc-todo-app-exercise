import grpc
from concurrent import futures
<<<<<<< HEAD

import todo_app_pb2_grpc as pb2_grpc
from todo import Todo


class TodoAppServer(pb2_grpc.TodoServiceServicer):
    def __init__(self):
        self.todo = Todo()

    def AddTodo(self, request, context):
        response = self.todo.add_todo(request)
        return response

    def ListAllTodos(self, request, context):
        response = self.todo.list_all_todos(request)
        return response
=======
import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc
from db import TodoDB


class TodoAppServer(pb2_grpc.TodoServiceServicer):
    def __init__(self, todo_db):
        self.todo_db = todo_db

    def _check_for_todo(self, id):
        try:
            with self.todo_db.db_conn as db_conn:
                cursor = db_conn.cursor()
                sql = "select 1 from todos where id=?"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
                if result:
                    return True
                else:
                    return False
        except:
            raise

    def AddTodo(self, request, context):
        try:
            if len(request.title) == 0:
                raise Exception("Title cannot be empty")
            # Add user id validation
            with self.todo_db.db_conn as db_conn:
                sql = "insert into todos(title,user_id,status) values(?,?,?) "
                val = (request.title, request.user_id, request.status)
                cursor = db_conn.cursor()
                cursor.execute(sql, val)
                inserted_id = cursor.lastrowid
                return pb2.Todo(
                    id=inserted_id,
                    user_id=request.user_id,
                    title=request.title,
                    status=request.status,
                )
        except:
            raise

    def GetUserTodos(self, request, context):
        try:
            with self.todo_db.db_conn as db_conn:
                cursor = db_conn.cursor()
                sql = "select id,user_id,title,status from todos where user_id=?"
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

    def DeleteTodo(self, request, context):
        try:
            with self.todo_db.db_conn as db_conn:
                if not self._check_for_todo(request.id):
                    raise Exception(
                        f"Todo with an id {request.id} donot exist, so it cannot be deleted"
                    )
                cursor = db_conn.cursor()
                sql = "delete from todos where id = ? "
                val = (request.id,)
                cursor.execute(sql, val)
                print("Todo item removed")
                return pb2.EmptyResponse()
        except:
            raise

    def EditTodo(self, request, context):
        try:
            with self.todo_db.db_conn as db_conn:
                if not self._check_for_todo(request.id):
                    raise Exception(
                        f"Todo with an id {request.id} donot exist, so it cannot be deleted"
                    )
                cursor = db_conn.cursor()
                update_sql = "UPDATE todos SET"
                update_params = []
                if request.title:
                    update_sql += " title=?,"
                    update_params.append(request.title)
                if request.status:
                    update_sql += " status=?,"
                    update_params.append(request.status)
                update_sql = update_sql.rstrip(",")
                update_sql += " WHERE id=? "
                update_params.extend([request.id])
                cursor.execute(update_sql, update_params)
                sql = "select id,user_id,title,status from todos where id=?"
                val = (request.id,)
                cursor.execute(sql, val)
                result = cursor.fetchall()
                if result:
                    row = result[0]
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
>>>>>>> 38f18660d5cfdb0db7ee0b71efac5efaff5a9d95


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TodoServiceServicer_to_server(TodoAppServer(TodoDB()), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Running the gRPC server at localhost:50051")
    serve()
