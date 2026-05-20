# task-management-system
Python To-Do App for ITP Final Project


## Introduction

Task Management System is a Python application created for the Introduction to Programming 2 final project.

The program helps users manage tasks and deadlines. Users can add, edit, delete, and complete tasks. The system also allows sorting tasks by priority and deadline, detecting overdue tasks, and generating statistics.

This project demonstrates the use of Python programming concepts such as:
- Object-Oriented Programming (OOP)
- File handling with JSON
- Collections and data structures
- Algorithms and sorting
- Exception handling
- Testing
- Modular project structure

---

# Features

## Main Features

- Add new tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Set priorities:
  - low
  - medium
  - high
- Set deadlines
- Sort tasks by priority and deadline
- Detect overdue tasks
- Generate completion statistics
- Save and load tasks using JSON files

---

# Technologies Used

- Python 3
- JSON
- OOP (Object-Oriented Programming)
- GitHub
- Unit Testing

---

# Project Structure

```text
task-management-system/
│
├── data/
│   └── tasks.json
│
├── models/
│   └── task.py
│
├── services/
│   ├── task_manager.py
│   ├── file_manager.py
│   └── report_generator.py
│
├── utils/
│   └── validator.py
│
├── tests/
│   └── test_tasks.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Classes Description

## Task
Represents a single task.

### Attributes
- id
- title
- description
- priority
- deadline
- status

### Methods
- mark_completed()
- update_task()
- to_dict()

---

## TaskManager
Manages all tasks in the system.

### Methods
- add_task()
- delete_task()
- edit_task()
- find_task()
- sort_tasks()
- show_overdue_tasks()
- show_statistics()

---

## FileManager
Handles reading and writing JSON files.

### Methods
- save_to_file()
- load_from_file()

---

## Validator
Validates task data such as:
- priority
- status
- deadline format

---

# Data Structures Used

The project uses several Python collections:

- List → storing tasks
- Dictionary → fast task lookup by ID
- Tuple → sorting by priority and deadline
- Set → unique statuses or priorities

The dictionary structure improves efficiency because task search works in O(1) time instead of O(n).

---

# Advanced Python Features

The project uses advanced Python concepts such as:

- lambda functions
- generators
- regular expressions
- decorators

Example:
```python
tasks.sort(key=lambda x: x.deadline)
```

---

# File Handling

The program stores task information in a JSON file.

Example format:

```json
[
  {
    "id": 1,
    "title": "Finish project",
    "description": "Complete final project",
    "priority": "high",
    "deadline": "2026-05-20",
    "status": "pending"
  }
]
```

---

# Testing

The project includes basic unit tests.

Test cases include:
- adding tasks
- invalid input validation
- overdue task detection
- sorting correctness

---

# How to Run the Project

## Step 1
Clone the repository:

```bash
git clone https://github.com/your-username/task-management-system.git
```

## Step 2
Open the project folder.

## Step 3
Run the program:

```bash
python main.py
```

---

# Example Menu

```text
1. Add task
2. Edit task
3. Delete task
4. Show all tasks
5. Show overdue tasks
6. Show statistics
7. Save and Exit
```

---

# Team Members

- A
- Member 2
- Member 3
- Member 4

---

# Contribution Breakdown

## Member 1
- Task class
- OOP structure

## Member 2
- JSON file handling
- Validation system

## Member 3
- Sorting and statistics
- Overdue task system

## Member 4
- Main menu
- Testing
- README and presentation

---

# Challenges Faced

Some challenges during development included:
- validating date formats
- implementing sorting algorithms
- detecting overdue tasks
- organizing project modules

---

# Conclusion

This project helped improve our understanding of Python programming, Object-Oriented Programming, algorithms, and teamwork using GitHub.

The application simulates a real-world task management system and demonstrates practical software development skills.
