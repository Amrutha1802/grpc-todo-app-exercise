import grpc
import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc


class TodoClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = pb2_grpc.TodoServiceStub(self.channel)

    def add_todo(self):
        request = pb2.Todo(title="complete grpc exercise", status=2)
        response = self.stub.AddTodo(request)
        return response

    def list_all(self):
        request = pb2.ListAllTodosRequest()
        response = self.stub.ListAllTodos(request)
        return response


if __name__ == "__main__":
    client = TodoClient()
    todos_response = client.list_all()
    print("All Todos:")
    for todo in todos_response.todos:
        print(todo)
    todos_response = client.add_todo()
    print("todo is")
    print(todos_response)
