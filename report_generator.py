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

    def generate_priority_task_report(self):
        high=0
        medium=0
        low=0
        for task in self.tasks:
            if task["status"]=="high":
                high+=1
            elif task["status"]=="medium":
                medium+=1
            elif task["status"]=="low":
                low+=1
        print("\nHigh priority tasks report:")
        print("High priority tasks:"+str(high))
        print("Medium priority tasks:"+str(medium))
        print("Low priority tasks:"+str(low))
