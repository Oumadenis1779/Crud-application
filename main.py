import os

# File path for storing tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        print("Tasks file not found. Creating a new one.")
    except Exception as e:
        print(f"Error loading tasks: {e}")
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Function to add a new task
def add_task(task, tasks):
    tasks.append(task)
    save_tasks(tasks)

# Function to delete a task
def delete_task(index, tasks):
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
    else:
        print("Invalid task index.")

# Function to display tasks
def display_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task, tasks)
            print("Task added successfully.")
        elif choice == "2":
            display_tasks(tasks)
            try:
                index = int(input("Enter task index to delete: ")) - 1
                delete_task(index, tasks)
                print("Task deleted successfully.")
            except ValueError:
                print("Invalid index. Please enter a number.")
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
