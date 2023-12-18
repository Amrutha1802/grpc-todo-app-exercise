import grpc
import todo_app_pb2 as pb2
import todo_app_pb2_grpc as pb2_grpc


class TodoClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = pb2_grpc.TodoServiceStub(self.channel)

    def add_todo(self):
        request = pb2.Todo(user_id=2, title="study mysql", status=2)
        response = self.stub.AddTodo(request)
        return response

    def list_all(self):
        request = pb2.User(id=2)
        print(request)
        response = self.stub.GetUserTodos(request)
        return response

    def delete_todo(self):
        request = pb2.DeleteTodoRequest(id=3)
        response = self.stub.DeleteTodo(request)
        return response

    def edit_todo(self):
        request = pb2.Todo(id=5, title="study python", status=2)
        response = self.stub.EditTodo(request)
        return response


if __name__ == "__main__":
    client = TodoClient()
    todos_response = client.add_todo()
    print(todos_response)
    print("edit todo")
    edit_response = client.edit_todo()
    print(edit_response)
    todos_of_user = client.list_all()
    for todo in todos_of_user.todos:
        print(todo)
