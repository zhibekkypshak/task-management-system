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
            "tittle":title,
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









