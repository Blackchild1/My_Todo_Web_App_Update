FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def make_dict(key, value):
    return {key: value}


def get_doc(filepath):
    """ Read a text file and return a string
    containing it content.
     """
    with open(filepath, "r") as file:
        content = file.read()
    return content


def write_doc(content, filepath):
    """Get a content in str format and write in
    a .txt file in the directory
    """
    with open(filepath, "w") as file:
        file.write(content)


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
