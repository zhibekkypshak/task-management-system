import json
import os

class FileManager:
    def __init__(self, filepath="data/tasks.json"):
        self.filepath = filepath
