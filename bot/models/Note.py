from .Fields import Id, Text
from nanoid import generate as generateId
from datetime import datetime

class Note:
    def __init__(self, value):
        self.text = Text(value)
        self.id = Id(generateId('1234567890abcdef', size=4))
        self.createdAt = datetime.now()

    def edit(self, new_value: str):
        if new_value:
            self.text.value = new_value

    def __str__(self):
        return f"{self.id} | {self.createdAt} | {self.text}"
    
    def __repr__(self):
        return f"Note({self.id=}, {self.createdAt=}, {self.text=})"