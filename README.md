# ToDo Application with gRPC, Protocol Buffers, and SQLite3

This is a simple ToDo application implemented using gRPC, Protocol Buffers, and SQLite3 in Python. The application allows you to add ToDo items and list all existing ToDo items.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- gRPC (install with `pip install grpcio`)
- SQLite3 (usually comes with Python)

Create a mysql database: todo

### To generate pb2 and pb2_grpc files

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. todo_app.proto`

### To run grpc server

`python todo_server.py`

The server will start at localhost:50051

### gRPC Client

You can use the provided gRPC client to interact with the server. Refer to the todo_app_client.py file for examples on how to use the client.

`python client.py`

#### gRPC Service Methods

##### AddTodo

Adds a new Todo item.

`rpc AddTodo (Todo) returns (Todo);`

#### ListAllTodos

##### Lists all existing ToDo items.

`rpc ListAllTodos (Empty) returns (ListAllTodosResponse);`

### Project Structure

- todo_app_server.py: Implementation of the gRPC server.
- todo_app_client.py: Example client to interact with the gRPC server.
- todo_app.proto: Protocol Buffers definition file.
- db.py: SQLite3 database setup.
- todo_app_pb2.py and todo_app_pb2_grpc.py: Generated files from the Protocol Buffers definition.
