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



