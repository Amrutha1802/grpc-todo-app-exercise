import grpc
from concurrent import futures

import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc
from db import TodoDB
from todo import Todo


class TodoAppServer(pb2_grpc.TodoServiceServicer):
    def __init__(self, todo_db):
        self.todo_db = todo_db
        self.todo = Todo()

    def AddTodo(self, request, context):
        resp = self.todo.add_todo(request)
        return resp


    def ListAllTodos(self, request, context):
        try:
            with self.todo_db.db_conn as db_conn:
                cursor = db_conn.cursor()
                cursor.execute("SELECT id, title, status FROM todo_items")
                rows = cursor.fetchall()
                todos_list = [
                    {"id": row[0], "title": row[1], "status": row[2]} for row in rows
                ]
            return pb2.ListAllTodosResponse(todos=todos_list)
        except:
            raise


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TodoServiceServicer_to_server(TodoAppServer(TodoDB()), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Running the gRPC server at localhost:50051")
    serve()
