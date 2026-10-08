TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from the file."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return [line.rstrip("\n") for line in file]
    except FileNotFoundError:
        return []  # No saved tasks yet
    except OSError as error:
        print(f"Could not read the task file: {error}")
        return []


def save_tasks(tasks):
    """Save tasks to the file."""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
    except OSError as error:
        print(f"Could not save the task file: {error}")


def add_task(tasks):
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("Your task list is empty.")
        return

    print("\nCurrent tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def remove_completed_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("Enter the number of the completed task: "))
        removed_task = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Removed: {removed_task}")
    except ValueError:
        print("Please enter a whole-number task number.")
    except IndexError:
        print("That task number is not in the list.")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add task")
        print("2. Remove completed task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_completed_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye.")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()