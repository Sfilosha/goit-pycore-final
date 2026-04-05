from datetime import datetime
import re

class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Text(Field):
    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("Note text cannot be empty.")
        super().__init__(value.strip())

class Address(Field):
    def __init__(self, value: str):
        self.address = value
        super().__init__(value)

class Phone(Field):
    def __init__(self, value: str):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Phone number must contain exactly 10 digits.")
        self.phone = value
        super().__init__(value)

class Email(Field):
    def __init__(self, value: str):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not (re.fullmatch(email_pattern, value)):
            raise ValueError("Please provide email in valid format")
        self.email = value
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Id(Field):
    pass

class Tag(Field):
    def __init__(self, value: str):
        if not value or not value.strip() or " " in value:
            raise ValueError("Tag must be a single word without spaces.")
        super().__init__(value.strip().lower())