tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['name']}")


def add_task():
    name = input("\nEnter a task: ").strip()

    if not name:
        print("Task cannot be empty.")
        return

    tasks.append({
        "name": name,
        "done": False
    })

    print("Task added!")


def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nWhich task did you complete? "))
        tasks[number - 1]["done"] = True
        print("Task completed!")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nWhich task do you want to delete? "))
        removed = tasks.pop(number - 1)
        print(f"Deleted: {removed['name']}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()