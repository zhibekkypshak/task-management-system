class ReportGenerator:
    def __init__(self, tasks):
        self.tasks=tasks

    def generate_completed_report(self):
        completed_tasks=[
            task for task in self.tasks
            if task["status"]=="completed"
        ]
        print("\nCompleted tasks report:")
        if completed_tasks:
            for task in completed_tasks:
                print(task)
            else:
                print("No completed tasks")

