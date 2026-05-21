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
