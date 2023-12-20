import grpc
from concurrent import futures

import todo_app_pb2_grpc as pb2_grpc
from todo import TodoDB


class TodoAppServer(pb2_grpc.TodoServiceServicer):
    def __init__(self):
        self.todo_db = TodoDB()

    def AddTodo(self, request, context):
        response = self.todo_db.add_todo(request)
        return response

    def GetUserTodos(self, request, context):
        response = self.todo_db.get_user_todos(request)
        return response

    def DeleteTodo(self, request, context):
        response = self.todo_db.delete_todo(request)
        return response

    def EditTodo(self, request, context):
        response = self.todo_db.edit_todo(request)
        return response

    def AddUser(self, request, context):
        response = self.todo_db.add_user(request)
        return response

    def GetUsers(self, request, context):
        response = self.todo_db.get_users()
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TodoServiceServicer_to_server(TodoAppServer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Running the gRPC server at localhost:50051")
    serve()
