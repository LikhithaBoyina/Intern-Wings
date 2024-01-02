import os

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")

def add_task(tasks, new_task):
    tasks.append(new_task)

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task.strip()}")
    else:
        print("Invalid task index.")

def save_tasks(tasks, filename='tasks.txt'):
    with open(filename, 'w') as file:
        file.writelines(tasks)

def load_tasks(filename='tasks.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.readlines()
    else:
        return []

def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List Application ===")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the task: ")
            add_task(tasks, new_task + '\n')
            save_tasks(tasks)
            print("Task added successfully.")
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
            save_tasks(tasks)
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
