# File path for storing tasks
TASKS_FILE = "tasks.txt"

# Create tasks.txt file if it doesn't exist
def create_tasks_file():
    try:
        with open(TASKS_FILE, "a") as file:
            pass  # Just creating an empty file
        print(f"{TASKS_FILE} created successfully.")
    except Exception as e:
        print(f"Error creating {TASKS_FILE}: {e}")

# Call the function to create the tasks file
create_tasks_file()
