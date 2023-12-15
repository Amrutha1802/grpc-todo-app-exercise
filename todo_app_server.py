import grpc
from concurrent import futures
import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc
import db as mydb
import sqlite3

connection = sqlite3.connect("todo.db", check_same_thread=False)


class TodoAppServer(pb2_grpc.TodoServiceServicer):
    def AddTodo(self, request, context):
        return mydb.add_todo(connection, request, pb2)

    def ListAllTodos(self, request, context):
        return mydb.get_all_todos(connection, request, pb2)

    def DeleteTodo(self, request, context):
        return mydb.delete_todo(connection, request, pb2)

    def EditTodo(self, request, context):
        return mydb.edit_todo(connection, request, pb2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TodoServiceServicer_to_server(TodoAppServer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Running the gRPC server at localhost:50051")
    serve()
