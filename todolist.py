todo_list = []

def menu():
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    

while True:
    menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f"Task '{task}' added.")
    elif choice == '2':
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
    elif choice == '3':
        if not todo_list:
            print("No tasks to remove.")
        else:
            print("Tasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        print("Exiting the to-do list application. Goodbye!")
        break   
    else:
        print("Invalid choice. Please select a valid option.")
        
        