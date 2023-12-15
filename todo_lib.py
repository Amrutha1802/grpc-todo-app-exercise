
def add_todo(request):
    title = request.title

    if len(title) == 0:
        raise Exception("title cannot be empty"
    # return todo pb2
