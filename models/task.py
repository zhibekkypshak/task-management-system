class Task:
    def __init__(self, task_id, title, description, priority, deadline, status = "pending"):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline

        self.__status = status

    def get_status(self):
            return self.__status
        
    def set_status(self, new_status):
            allowed_statuses = [
                "pending",
                "in_progress",
                "completed"
            ]

            if new_status in allowed_statuses:
                self.__status = new_status
            else:
                print("invalid status")

        
    def mark_completed(self):
            self.__status = "completed"

    def update_task(self, title = None,
                        description = None,
                        priority = None,
                        deadline = None):
        if title:
                self.title = title

        if description:
                self.description = description

        if priority:
                self.priority = priority
            
        if deadline:
                self.deadline = deadline
            
        def dict(self):
            return {"id": self.id, "title": self.title, "description": self.description, "priority": self.priority, "deadline": self.deadline, "status": self.__status}
        
        @classmethod 
        def obj(c, data):
            return c(data["id"], data["title"], data["description"], data["priority"], data["deadline"], data["status"]
            )
        
        class subtask(Task):
            def __init__(self, task_id, title, description, priority, deadline, status="pending"):
                super().__init__(task_id, title, description, priority, deadline, status)
                self.important = True