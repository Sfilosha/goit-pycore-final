
import bot.helpers.logger as logger
from bot.models.AddressBook import AddressBook
from bot.models.Record import Record
import questionary


# CONTACT COMMANDS
@logger.input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    existing_record = book.find_by_name(name)
    
    if existing_record:
        return existing_record

    if len(name) > 1:
        new_record = Record(name)
        book.add_record(new_record)
        if phone:
            new_record.add_phone(phone)
        return f"✅ Contact '{name}' added."
    raise ValueError(f'Name should contain at least 1 letter')

@logger.input_error
def delete_contact(record, book: AddressBook):
    book.delete(record.name.value)
    return f"✅ Contact {record.name.value} deleted."

@logger.input_error
def edit_contact_name(record, new_name):
    if new_name:
        record.edit_name(new_name)
        return "✅ Name updated."
    raise ValueError("❌ Name cannot be empty.")

@logger.input_error
def add_phone(record):
    new_val = questionary.text("Enter new phone number:").ask()
    if new_val:
        record.add_phone(new_val)
        return f"✅ Phone added!"
    raise ValueError("❌ Phone cannot be empty.")

@logger.input_error
def edit_phone(record, phone, new_val):
    if new_val:
        record.edit_phone(phone.value, new_val)
        return "✅ Phone updated!"
    raise ValueError("❌ Phone cannot be updated.")

@logger.input_error
def delete_phone(record, phone):
    record.remove_phone(phone.value)
    return f"🗑️ Phone deleted."

@logger.input_error
def append_phone_to_existing(record, phone):
    record.add_phone(phone)
    return f"✅ Phone added to existing contact '{record.name.value}'."

@logger.input_error
def show_all(book: AddressBook):
    if not book.data:
        return "No contacts found."
    result = []
    for i, contact in enumerate(book.data.values(), 1):
        result.append(f"{contact}")
    return "\n".join(result)

def birthdays(book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next week."
    print("Upcoming birthdays in next 7 days:")
    return "\n".join(f"{item['name']}: {item['congratulation_date']}" for item in upcoming)
