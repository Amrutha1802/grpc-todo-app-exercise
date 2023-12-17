import grpc
import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc


class TodoClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = pb2_grpc.TodoServiceStub(self.channel)

    def add_todo(self):
        pass

    def list_all(self):
        request = pb2.User(id=1)
        print(request)
        response = self.stub.GetUserTodos(request)
        return response

    def delete_todo(self):
        request = pb2.DeleteTodoRequest(id=34)
        response = self.stub.DeleteTodo(request)
        return response


if __name__ == "__main__":
    client = TodoClient()
    todos_response = client.list_all()
    for list in todos_response:
        print(list)
