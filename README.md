# Todo Application with gRPC, Protocol Buffers, and SQLite3

This is a simple Todo application implemented using gRPC, Protocol Buffers, and SQLite3 in Python. The application allows you to add Todo items of a user, to add a user,edit todo, list all todos of a user, delete a todo,list all users.

## Prerequisites

Before running the application, install following dependencies:

- Python 3.8.10
- SQLite3 (usually comes with Python)

`pip install requirements.txt`

Create a sqlite3 database: todo

### To generate pb2 and pb2_grpc files

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. todo_app.proto`

### To run grpc server

`python todo_app_server.py`

The server will start at localhost:50051

### gRPC Client

You can use the provided gRPC client to interact with the server. Refer to the `todo_app_client.py` file for examples on how to use the client.

`python todo_app_client.py`

#### gRPC Service Methods

##### AddTodo

Adds a new Todo item.

`rpc AddTodo (Todo) returns (Todo){}`

##### AddUser

Adds a new User.

`rpc AddUser(User) returns (User) {}`

#### GetUsers

Lists all existing users.

`rpc GetUsers(EmptyRequest) returns (UsersList) {}`

#### GetUserTodos

Lists all existing Todo items of a user.

`rpc ListAllTodos (Empty) returns (ListAllTodosResponse {}`

#### DeleteTodo

Deletes a todo with a given id

`rpc DeleteTodo(DeleteTodoRequest) returns (EmptyResponse) {}`

#### EditTodo

Updates todo with given title and status

`rpc EditTodo(Todo) returns (Todo) {}`

### Project Structure

- todo_app_server.py: Implementation of the gRPC server.
- todo_app_client.py: Example client to interact with the gRPC server.
- todo_app.proto: Protocol Buffers definition file.
- todo.py: SQLite3 database setup.
- todo_app_pb2.py and todo_app_pb2_grpc.py: Generated files from the Protocol Buffers definition.
