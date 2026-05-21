from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print("Task removed")
                return
        print("Task not found")

    def find_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def edit_task(self, task_id, new_title=None, new_priority=None, new_deadline=None, new_status=None):
        task=self.find_task(task_id)
        if task:
            if new_title:
                task["title"] = new_title
            if new_priority:
                task["priority"] = new_priority
            if new_deadline:
                task["deadline"] = new_deadline
            if new_status:
                task["status"] = new_status
            print("Task updated")
        else:
            print("Task not found")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return
        for task in self.tasks:
            print(task)

    def sort_tasks(self):
        priority_order = {
            "high": 1,
            "medium": 2,
            "low": 3
        }
        self.tasks.sort(key=lambda task:(priority_order[task["priority"]], task["deadline"]))
        print("Sorted tasks")

    def show_overdue_tasks(self):
        today=datetime.today()
        overdue_tasks=[]
        for task in self.tasks:
            deadline=datetime.strptime(task["deadline"], "%Y-%m-%d")
            if deadline < today and task["status"] != "completed":
                overdue_tasks.append(task)
        if overdue_tasks:
            print("\nOverdue tasks")
            for task in overdue_tasks:
                print(task)
        else:
            print("No overdue tasks found")

    def show_statistics(self):
        total_tasks = len(self.tasks)

        completed_tasks = sum(
            1 for task in self.tasks
            if task["status"] == "completed"
        )
        pending_tasks = sum(
            1 for task in self.tasks
            if task["status"] == "pending"
        )
        in_progress_tasks = sum(
            1 for task in self.tasks
            if task["status"] == "in_progress"
        )
        if total_tasks>0:
            completion_rate=(completed_tasks/total_tasks)*100
        else:
            completion_rate=0
        print("\nTask statistics")
        print("Total tasks:"+str(total_tasks))
        print("Completed tasks:"+str(completed_tasks))
        print("Pending tasks:"+str(pending_tasks))
        print("In-progress tasks:"+str(in_progress_tasks))
        print("Completion rate:"+str(completion_rate))




