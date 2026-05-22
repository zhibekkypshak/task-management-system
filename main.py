from services.file_manager import FileManager
from utils.validator import Validator

def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add task")
    print("2. Edit task")
    print("3. Delete task")
    print("4. Show tasks")
    print("5. Statistics")
    print("0. Exit")
    return input("Choose: ").strip()

def add_task(tasks):
    title = input("Title: ").strip()
    priority = input("Priority (low/medium/high: ").strip()
    deadline = input("Deadline (YYYY-MM-DD): ").strip()

    try:
        Validator.validate_priority(priority)
        Validator.validate_deadline(deadline)

        task = {
            "id": len(tasks) + 1,
            "title":title,
            "description":"",
            "priority": priority,
            "deadline":deadline,
            "status": "pending"
        }
        tasks.append(task)
        print("Task added!")

    except ValueError as e:
        print(f"Error: {e}")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"\n[{task['id']}] {task['title']}")
        print(f"    Priority: {task['priority']}")
        print(f"    Deadline: {task['deadline']}")
        print(f"    Status:    {task['status']}")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
        task = next((t for t in tasks if t["id"] == task_id), None)
        if task:
            tasks.remove(task)
            print("Task deleted!")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid ID.")


def edit_task(tasks):
    show_tasks(tasks)
    try:
        task_id =int(input("Enter task ID too edit: "))
        task = next((t for t in tasks if t["id"] == task_id),None)
        if not task:
            print("Task not found.")
            return

        print("Leave blank to keep current value.")
        title = input(f"Title [{task['title']}]: ").strip()
        priority = input(f"Priority [{task['priority']}]: ").strip()
        deadline = input(f"Deadline [{task['deadline']}]: ").strip()
        status = input(f"Status [{task['status']}]: ").strip()

        try:
            if priority:
                Validator.validate_priority(priority)
                task["priority"] = priority
            if deadline :
                Validator.validate_deadline(deadline)
                task["deadline"]= deadline
            if title:
                task["title"]=title
            if status:
                Validator.validate_status(status)
                task["status"]=status
            print("Task updated!")

        except ValueError as e:
            print(f"Error: {e}")
    except ValueError:
        print("Invalid ID.")


def show_statistics(tasks):
    if not tasks:
        print("No tasks found.")
        return
    total = len(tasks)
    completed = sum(1 for t in tasks if t["status"] == "completed")
    in_progress = sum(1 for t in tasks if t["status"] == "in_progress")
    pending = sum(1 for t in tasks if t ["status"] == "pending")

    high = sum(1 for t in tasks if t["priority"] == "high")
    medium = sum (1 for t in tasks if t["priority"] == "medium")
    low = sum(1 for t in tasks if t["priority"] == "low")

    print("\n=== Statistics ===")
    print(f"Total tasks:    {total}")
    print(f"Completed:      {completed}")
    print(f"In progress:    {in_progress}")
    print(f"Pending:        {pending}")
    print(f"\nHigh priority:    {high}")
    print(f"Medium priority: {medium}")
    print(f"Low priority:    {low}")


def run():
    fm = FileManager()
    tasks = fm.load_from_file()

    while True:
        choice = show_menu()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            show_tasks(tasks)
        elif choice == "5":
            show_statistics(tasks)
        elif choice == "0":
            fm.save_to_file(tasks)
            print("Saved.Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__=="__main__":
    run()










