import grpc
from concurrent import futures
import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc
import db as mydb
import sqlite3

# connection = sqlite3.connect("todo.db", check_same_thread=False)
db_conn = sqlite3.connect("todo.db", check_same_thread=False)
from db import TodoDB


class TodoAppServer(pb2_grpc.TodoServiceServicer):
    def __init__(self, todo_db):
        self.todo_db = todo_db

    def AddTodo(self, request, context):
        """
        input
        creating todo in db

        input is in pb
        db functions operate with python data structures
        """
        return add_todo(request)

    def ListAllTodos(self, request, context):
        return mydb.get_all_todos(db_conn, pb2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TodoServiceServicer_to_server(TodoAppServer(TodoDB()), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Running the gRPC server at localhost:50051")
    serve()
