import json
import os

class FileManager:
    def __init__(self, filepath="data/tasks.json"):
        self.filepath = filepath
        
    def save_to_file(self, tasks):
        try:
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(tasks, f, indent=4, ensure_ascii=False)
            print("Tasks saved successfully")
        except IOError as e:
            print(f"Error saving tasks: {e}")
            
    def load_from_file(self):
        try:
            if not os.path.exists(self.filepath):
                print("No saved tasks found, starting fresh")
                return []
            with open(self.filepath, "r", encoding="utf-8") as f:
                tasks = json.load(f)
            print(f"Loaded {len(tasks)} task(s) from file")
            return tasks
        except json.JSONDecodeError as e:
            print(f"Error reading file (invalid JSON): {e}")
            return []
        except IOError as e:
            print(f"Error opening file: {e}")
            return []


