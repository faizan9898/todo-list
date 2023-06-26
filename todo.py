tasks = []

def show_menu():
    print("===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("===== Tasks =====")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_task_completed():
    view_tasks()
    if len(tasks) == 0:
        return

    task_index = int(input("Enter the task number to mark as completed: ")) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
    else:
        tasks[task_index] = f"[COMPLETED] {tasks[task_index]}"
        print("Task marked as completed!")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return

    task_index = int(input("Enter the task number to delete: ")) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
    else:
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task}' deleted successfully!")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
