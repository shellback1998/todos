FILEPATH = "todofiles/todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do itesms.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath_arg=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath_arg, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())