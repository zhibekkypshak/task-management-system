class ReportGenerator:
    def __init__(self, tasks):
        self.tasks=tasks

    def generate_completed_report(self):
        completed_tasks = [
            task for task in self.tasks
            if task["status"] == "completed"
        ]
        print("\nCompleted tasks report:")
        if completed_tasks:
            for task in completed_tasks:
                print(task)
        else:
            print("No completed tasks")

    def generate_priority_task_report(self):
        high = 0
        medium = 0
        low = 0
        for task in self.tasks:
            if task["priority"] == "high":
                high+=1
            elif task["priority"] == "medium":
                medium+=1
            elif task["priority"] == "low":
                low+=1
        print("\nPriority tasks report:")
        print("High priority tasks:" + str(high))
        print("Medium priority tasks:" + str(medium))
        print("Low priority tasks:" + str(low))

    def generate_pending_report(self):
        pending_tasks=[
            task for task in self.tasks
            if task["status"]=="pending"
        ]
        print("\nPending tasks report:")
        if pending_tasks:
            for task in pending_tasks:
                print(task)
        else:
            print("No pending tasks")

    def generate_in_progress_report(self):
        in_progress_tasks=[
            task for task in self.tasks
            if task["status"]=="in_progress"
        ]
        print("\nIn-progress tasks report:")
        if in_progress_tasks:
            for task in in_progress_tasks:
                print(task)
        else:
            print("No in-progress tasks")
