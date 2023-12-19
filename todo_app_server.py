import grpc
from concurrent import futures

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


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TodoServiceServicer_to_server(TodoAppServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Running the gRPC server at localhost:50051")
    serve()
