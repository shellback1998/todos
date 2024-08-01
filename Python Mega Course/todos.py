# def readfile(file):
#     with open(file, 'r') as f:
#         todos = file.readlines()
#     return todos
#
# def writefile(file):
#     with open(file, "w") as f:
#         f.writelines(todos)


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            # readfile('files/todos.txt')

            # todos.append(todo)

            # file = open('files/todos.txt', 'w')
            # file.writelines(todos)
            # file.close()

            with open('files/todos.txt', 'w') as f:
                f.writelines(todos)

            # writefile('files/todos.txt')

        case 'show':

            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('files/todos.txt', 'r') as f:
                todos = f.readlines()

            # readfile("files/todos.txt")

            # new_todos = [item.strip('\') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)


        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('files/todos.txt', 'r') as f:
                todos = f.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open('files/todos.txt', 'w') as f:
                f.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)

            with open('files/todos.txt', 'r') as f:
                todos = f.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as f:
                f.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break
            print("Bye")
