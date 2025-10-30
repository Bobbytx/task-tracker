tasks = []
completedTasks = []

def addTask(task: str) -> None:
    cleaned = task.strip() #strips spaces and stores cleaned string
    if cleaned: #checks if string is empty or not
        tasks.append(cleaned)
        print(f'\n"{cleaned}" added to your list.\n')
    else:
        print("\nTask cannot be empty.\n")

def viewTasks():
    print()
    if not tasks:
        print("There are no tasks to view.\n")
        return

    print("List of tasks:\n")
    for num, task in enumerate(tasks, start = 1):
        print(f"{num}: {task}")
    print("\n--- End of list ---\n")
        
def viewCompletedTasks():
    print()
    if completedTasks:
        print("Your completed tasks:\n")
        for num, task in enumerate(completedTasks, start = 1):
            print(f"{num}: {task}")
        print("\n--- End of list ---\n")
    else:
        print("There are no completed tasks.\n")
     
def completeTask(task) -> None:
    cleaned = task.strip()
    if cleaned in tasks:
        completedTasks.append(cleaned)
        tasks.remove(cleaned)
        print(f'\n"{cleaned}" marked complete.\n')
    else:
        print("\nThis task is not present.\n")

if __name__ == "__main__":
    while True:
        command = input("1. Add\n2. View\n3. Complete\n4. View Completed\n5. Quit\nChoose One: ").strip().lower()
        if command in ("add", "1"):
            task = input("\nEnter your task: ")
            addTask(task)
        elif command in ("view", "2"):
            viewTasks()
        elif command in ("complete", "3"):
            task = input("\nEnter task you completed: ")
            completeTask(task)
        elif command in ("view completed", "4"):
            viewCompletedTasks()
        elif command in ("quit", "5"):
            break
        else:
            print("\nThat's not an option. Try again.\n")
