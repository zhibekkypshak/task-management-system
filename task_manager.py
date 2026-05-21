class TaskManager:
    def __init__(self):
        self.tasks = []
    def add(self, task):
        self.tasks.append(task)
        print("Task added")