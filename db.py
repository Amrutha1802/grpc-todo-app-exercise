# implement ddl queries here


def check_for_id(mycursor, todo_id, user_id):
    """
    Checks if a todo with the given ID already exists in the database.

    Parameters:
    - mycursor (sqlite3.cursor): SQLite database cursor object.
    - todo_id (int): The ID of the todo to be checked.

    Raises:
    -Exception if todo with the given id exists

    """
    try:
        sql = "select 1 from todos where id=? and user_id=?"
        mycursor.execute(sql, (todo_id, user_id))
        result = mycursor.fetchone()
        if result:
            raise Exception(f"todo with an {todo_id} already exists")
    except Exception as e:
        raise e


def check_for_user(mycursor, user_id):
    """
    Checks if a user with user_id has todos in the database.

    Parameters:
    - mycursor (sqlite3.cursor): SQLite database cursor object.
    - user_id (int): The ID of the todo to be checked.

    Raises:
    -Exception if todo with the given id exists

    """
    try:
        sql = "select 1 from todos where user_id=? "
        mycursor.execute(sql, (user_id,))
        result = mycursor.fetchone()
        if result:
            return True
        else:
            return False
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

    """
    todo = {
        "id": request.id,
        "user_id": request.user_id,
        "title": request.title,
        "status": request.status,
    }
    try:
        mycursor = connection.cursor()
        check_for_id(mycursor, todo["id"])
        sql = "insert into todos_with_userId(id,user_id,title,status) values(?,?,?,?) "
        val = (todo["id"], todo["user_id"], todo["title"], todo["status"])
        mycursor.execute(sql, val)
        connection.commit()
        print("Todo item added")
        return pb2.Todo(
            id=request.id,
            user_id=request.user_id,
            title=request.title,
            status=request.status,
        )
    except connection.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mycursor:
            mycursor.close()


def edit_todo(connection, request, pb2):
    """
    Add a new todo to the SQLite database.

    Parameters:
    - connection (sqlite3.Connection): The SQLite database connection.
    - request: The request object containing todo information.
    - pb2: The protocol buffer module.

    Returns:
    - pb2.Todo: The newly added todo.

    """
    try:
        mycursor = connection.cursor()
        check_for_id(mycursor, request.id)
        sql = "update todos_with_userId SET title =?, status = ? WHERE id = ? AND user_id = ?;"
        val = (request.title, request.status, request.id, request.user_id)
        mycursor.execute(sql, val)
        connection.commit()
        print("Todo item added")
        return pb2.Todo(
            id=request.id,
            user_id=request.user_id,
            title=request.title,
            status=request.status,
        )
    except connection.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mycursor:
            mycursor.close()


def delete_todo(connection, request, pb2):
    """
    Add a new todo to the SQLite database.

    Parameters:
    - connection (sqlite3.Connection): The SQLite database connection.
    - request: The request object containing todo information.
    - pb2: The protocol buffer module.

    Returns:
    - pb2.Todo: The newly added todo.

    """
    try:
        mycursor = connection.cursor()
        check_for_id(mycursor, request.id)
        sql = "delete from todos_with_userId where id = ? and user_id = ?;"
        val = (request.id, request.user_id)
        mycursor.execute(sql, val)
        connection.commit()
        print("Todo item removed")
        return pb2.EmptyResponse()
    except connection.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mycursor:
            mycursor.close()


def get_all_todos(connection, request, pb2):
    """
    Retrieve all todos from the SQLite database.

    Parameters:
    - connection (sqlite3.Connection): The SQLite database connection.
    - pb2: The protocol buffer module.

    Returns:
    - pb2.ListAllTodosResponse: A response object containing a list of all todos.

    """
    try:
        mycursor = connection.cursor()
        if check_for_user(request.user_id):
            sql = "select id,title,status from todos where user_id=?"
            val = (request.user_id,)
            mycursor.execute(sql, val)
            result = mycursor.fetchall()
            todos_list = []
            for row in result:
                dict = {"id": row[0], "title": row[1], "status": row[2]}
                todos_list.append(dict)
            return pb2.ListAllTodosResponse(todos=todos_list)
        else:
            raise Exception(f"The user with given id {request.user_id} has no todo's")
    except connection.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mycursor:
            mycursor.close()
