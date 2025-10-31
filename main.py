import json

tasks = []
completed_tasks = []
STORAGE_FILE = "tasks.json"

def load_tasks():
    try:
        with open(STORAGE_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return
    except json.JSONDecodeError:
        return
    
    tasks[:] = data.get("pending", [])
    completed_tasks[:] = data.get("completed", [])
    
def save_tasks():
    data = {
        "pending": tasks,
        "completed": completed_tasks,
    }
    with open(STORAGE_FILE, "w") as file:
        json.dump(data, file, indent=2)
    

# created function for menu to simplify main while loop
def print_menu():
    """Return the formatted prompt shown for menu selection."""
    menu = (
        "1. Add\n"
        "2. View\n"
        "3. Complete\n"
        "4. View Completed\n"
        "5. Quit\n"
        "Choose One: "
    )
    return menu

def add_task(task: str) -> None:
    """Normalize and add a task to the pending list."""
    cleaned = task.strip() #strips spaces and stores cleaned string
    if cleaned: #checks if string is empty or not
        tasks.append(cleaned)
        save_tasks()
        print(f'\n"{cleaned}" added to your list.\n')
    else:
        print("\nTask cannot be empty.\n")

def view_tasks():
    """Display all pending tasks or a helpful message if empty."""
    print()
    if not tasks:
        print("There are no tasks to view.\n")
        return

    print("List of tasks:\n")
    for num, task in enumerate(tasks, start = 1):
        print(f"{num}: {task}")
    print("\n--- End of list ---\n")
        
def view_completed_tasks():
    """Display completed tasks when available."""
    print()
    if completed_tasks:
        print("Your completed tasks:\n")
        for num, task in enumerate(completed_tasks, start = 1):
            print(f"{num}: {task}")
        print("\n--- End of list ---\n")
    else:
        print("There are no completed tasks.\n")
     
def complete_task(task: str) -> None:
    """Move a task from pending to completed if present."""
    cleaned = task.strip()
    if cleaned in tasks:
        completed_tasks.append(cleaned)
        tasks.remove(cleaned)
        save_tasks()
        print(f'\n"{cleaned}" marked complete.\n')
    else:
        print("\nThis task is not present.\n")

# Helper functions used in while loop to call main functions
def handle_add():
    task = input("\nEnter your task: ")
    add_task(task)

def handle_view():
    view_tasks()

def handle_complete():
    if not tasks:
        print("\nThere are no tasks to complete.\n")
        return

    task = input("\nEnter task you completed: ")
    complete_task(task)

def handle_view_completed():
    view_completed_tasks()

ACTIONS = {
    "add": handle_add,
    "1": handle_add,
    "view": handle_view,
    "2": handle_view,
    "complete": handle_complete,
    "3": handle_complete,
    "view completed": handle_view_completed,
    "4": handle_view_completed,
}

def run_cli() -> None:
    #Run the interactive command loop.
    while True:
        command = input(print_menu()).strip().lower()
        action = ACTIONS.get(command)
        if action:
            action()
        elif command in {"quit", "5"}:
            break
        else:
            print("\nThat's not an option. Try again.\n")


if __name__ == "__main__":
    load_tasks()
    run_cli()
