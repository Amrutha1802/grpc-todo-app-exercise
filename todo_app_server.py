import grpc
from concurrent import futures
import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc
from db import TodoDB


class TodoAppServer(pb2_grpc.TodoServiceServicer):
    def __init__(self, todo_db):
        self.todo_db = todo_db

    def AddTodo(self, request, context):
        try:
            if len(request.title) == 0:
                raise Exception("title cannot be empty")
            self.todo_db.add_todo(request.title, request.status)
            return pb2.Todo(request)
        except:
            raise

    def ListAllTodos(self, request, context):
        try:
            todos_list = self.todo_db.list_all_todos()
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
