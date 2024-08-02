def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath_arg, todos_arg):
    with open(filepath_arg, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todofiles/todos.txt")

        todos.append(todo + "\n")

        write_todos("todofiles/todos.txt", todos)

    elif user_action.startswith("show"):

        todos = get_todos("todofiles/todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todofiles/todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("todofiles/todos.txt", todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos.pop(number - 1)

            todos = get_todos("todofiles/todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todofiles/todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("The command not valid.")
print("Bye")
