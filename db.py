# implement ddl queries here


def check_for_id(mycursor, todo_id):
    """
    Check if a todo with the given ID already exists in the database.

    Parameters:
    - mycursor (sqlite3.cursor): SQLite database cursor object.
    - todo_id (int): The ID of the todo to be checked.

    Raises:
    - Exception: If a todo with the given ID already exists in the database.
    """
    try:
        sql = "select 1 from todos where id=?"
        mycursor.execute(sql, (todo_id,))
        result = mycursor.fetchone()
        if result:
            raise Exception(f"todo with an {todo_id} already exists")
    except Exception as e:
        raise e


def add_todo(connection, request, pb2):
    """
    Add a new todo to the SQLite database.

    Parameters:
    - connection (sqlite3.Connection): The SQLite database connection.
    - request: The request object containing todo information.
    - pb2: The protocol buffer module.

    Returns:
    - pb2.Todo: The newly added todo.

    Raises:
    - sqlite3.Error: If there is an error in the SQLite database operation.
    - Exception: If there is an error during the addition of the todo.
    """
    todo = {"id": request.id, "title": request.title, "status": request.status}
    try:
        mycursor = connection.cursor()
        check_for_id(mycursor, todo["id"])
        sql = "insert into todos(id,title,status) values(?,?,?) "
        val = (todo["id"], todo["title"], todo["status"])
        mycursor.execute(sql, val)
        connection.commit()
        print("Todo item added")
        return pb2.Todo(id=request.id, title=request.title, status=request.status)
    except connection.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mycursor:
            mycursor.close()


def get_all_todos(connection, pb2):
    """
    Retrieve all todos from the SQLite database.

    Parameters:
    - connection (sqlite3.Connection): The SQLite database connection.
    - pb2: The protocol buffer module.

    Returns:
    - pb2.ListAllTodosResponse: A response object containing a list of all todos.

    Raises:
    - sqlite3.Error: If there is an error in the SQLite database operation.
    - Exception: If there is any other error during the retrieval of todos.
    """
    try:
        mycursor = connection.cursor()
        sql = "select id,title,status from todos"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        todos_list = []
        for row in result:
            dict = {"id": row[0], "title": row[1], "status": row[2]}
            todos_list.append(dict)
        return pb2.ListAllTodosResponse(todos=todos_list)
    except connection.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mycursor:
            mycursor.close()
