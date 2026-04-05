from .Fields import Phone, Name, Birthday, Id, Email, Address, Tag
from nanoid import generate as generateId

class Record:
    def __init__(self, name):
        self.id = Id(generateId('1234567890abcdef', size=4))
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None
        self.tags = []

    def add_phone(self, number: str):
        self.phones.append(Phone(number))

    def edit_name(self, value: str):
        self.name.value = value

    def remove_phone(self, number: str):
        phone = self.find_phone(number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError(f"Phone number {number} not found.")
    
    def edit_phone(self, old_number: str, new_number: str):
        old_phone_number = self.find_phone(old_number)
        if not old_phone_number:
            raise ValueError(f"Phone number {old_number} not found.")
        
        new_phone_number = Phone(new_number)
        old_phone_number.value = new_phone_number.value
    
    def find_phone(self, number: str):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None
    
    def add_birthday(self, date: str):
        self.birthday = Birthday(date)

    def remove_birthday(self):
        self.birthday = None

    def add_email(self, email: str):
        self.email = Email(email)
    
    def remove_email(self):
        self.email = None

    def add_address(self, address: str):
        self.address = Address(address)
    
    def remove_address(self):
        self.address = None

    def add_tag(self, tag_value: str):
        normalized_tag = tag_value.strip().lower()
        if any(t.value == normalized_tag for t in self.tags):
            raise ValueError(f"Tag '{normalized_tag}' already exists for this contact.")
        self.tags.append(Tag(normalized_tag))

    def remove_tag(self, tag_value: str):
        normalized_tag = tag_value.strip().lower()
        tag_to_remove = next((t for t in self.tags if t.value == normalized_tag), None)
        if tag_to_remove:
            self.tags.remove(tag_to_remove)
        else:
            raise ValueError(f"Tag '{normalized_tag}' not found in this contact.")

    def __str__(self):
        tags_str = ", ".join(f"#{t.value}" for t in self.tags) if self.tags else "No tags"
        return f"{self.id} | {self.name} | phones: {'; '.join(p.value for p in self.phones)} | birthday: {self.birthday} | email: {self.email} | address: {self.address} | tags: {tags_str}"