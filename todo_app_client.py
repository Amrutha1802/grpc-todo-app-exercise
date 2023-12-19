import grpc
import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc


class TodoClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = pb2_grpc.TodoServiceStub(self.channel)

    def add_todo(self):
        pass

    def list_all(self, request):
        response = self.stub.GetUserTodos(request)
        return response

    def delete_todo(self, request):
        response = self.stub.DeleteTodo(request)
        return response

    def edit_todo(self, request):
        response = self.stub.EditTodo(request)
        return response


if __name__ == "__main__":
    client = TodoClient()
    request = pb2.Todo(user_id=3, title="study sql")
    add_todo_response = client.add_todo(request)
    print(add_todo_response)
    print("editing a todo")
    request = pb2.Todo(id=5, title="learn python")
    # edit_response = client.edit_todo(request)
    # print(edit_response)
    # print("deleting a todo")
    # request = pb2.DeleteTodoRequest(id=20)
    # client.delete_todo(request)
    print("user todos")
    request = pb2.User(id=4)
    todos_of_user = client.list_all(request)
    for todo in todos_of_user.todos:
        print(todo)
    todos_response = client.add_todo()
    print("todo is")
    print(todos_response)
