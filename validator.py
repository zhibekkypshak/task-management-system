import re

ALLOWED_PRIORITIES = ["low", "medium", "high"]
ALLOWED_STATUSES = ["pending", "in_progress", "completed"]
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

class Validator:
