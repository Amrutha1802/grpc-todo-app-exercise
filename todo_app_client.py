import grpc
import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc


class TodoClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = pb2_grpc.TodoServiceStub(self.channel)

    def add_todo(self, request):
        response = self.stub.AddTodo(request)
        return response

    def list_all(self, request):
        response = self.stub.GetUserTodos(request)
        return response

    def delete_todo(self, request):
        response = self.stub.DeleteTodo(request)
        return response

    def edit_todo(self, request):
        response = self.stub.EditTodo(request)
        return response

    def add_user(self, request):
        response = self.stub.AddUser(request)
        return response

    def get_users(self):
        response = self.stub.GetUsers(request)
        return response


if __name__ == "__main__":
    client = TodoClient()
    req = pb2.User(name="User")
    res = client.add_user(req)
    print(res)
    request = pb2.Todo(user_id=3, title="todo2")
    add_todo_response = client.add_todo(request)
    print(add_todo_response)
    print("editing a todo")
    request = pb2.Todo(id=19, title="edit todo 19", status=2)
    edit_response = client.edit_todo(request)
    print(edit_response)
    print("deleting a todo")
    request = pb2.DeleteTodoRequest(id=21)
    client.delete_todo(request)
    print("user todos")
    request = pb2.User(id=3)
    todos_of_user = client.list_all(request)
    for todo in todos_of_user.todos:
        print(todo)
    users_list = client.get_users()
    print("users list is ")
    for user in users_list.users:
        print(user)
