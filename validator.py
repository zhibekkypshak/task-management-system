import re

ALLOWED_PRIORITIES = ["low", "medium", "high"]
ALLOWED_STATUSES = ["pending", "in_progress", "completed"]
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

class Validator:
    @staticmethod
    def validate_priority(priority):
        if priority not in ALLOWED_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Must be one of: {ALLOWED_PRIORITIES}")
        return True
 
    @staticmethod
    def validate_status(status):
        if status not in ALLOWED_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Must be one of: {ALLOWED_STATUSES}")
        return True
        
    @staticmethod
    def validate_deadline(deadline):
        """Check that deadline matches YYYY-MM-DD format using regex"""
        if not DATE_PATTERN.match(deadline):
            raise ValueError(
                f"Invalid deadline format '{deadline}'. Expected: YYYY-MM-DD"
            )
        return True
 
