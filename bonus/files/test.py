while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]
        print("You typed add")
        with open('../../Python Mega Course/app1/todofiles/todos.txt') as file:
            todos = file.readlines()
            print("you are within the with statement")
        todos.append(todo)
        print("just added the todo")
        with open('../../Python Mega Course/app1/todofiles/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open('../../Python Mega Course/app1/todofiles/todos.txt', 'r') as f:
            todos = f.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open('../../Python Mega Course/app1/todofiles/todos.txt', 'r') as f:
            todos = f.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open('../../Python Mega Course/app1/todofiles/todos.txt', 'w') as f:
            f.writelines(todos)

    elif 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))
        todos.pop(number - 1)

        with open('../../Python Mega Course/app1/todofiles/todos.txt', 'r') as f:
            todos = f.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('../../Python Mega Course/app1/todofiles/todos.txt', 'w') as f:
            f.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("The command is not valid.")
print("Bye")
