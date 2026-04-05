import bot.helpers.logger as logger
from bot.models.AddressBook import AddressBook
from bot.models.Record import Record
from bot.models.Errors import NotFoundError

# CONTACT COMMANDS
@logger.input_error
def add_contact(args, book: AddressBook):
    if not args:
        raise ValueError("❌ Please provide a name.")
    
    name = args[0]
    phone = args[1] if len(args) > 1 else None 
    
    contact = book.find_by_name(name)
    message = f"✅ Contact '{name}' updated."
    
    if contact is None:
        contact = Record(name)
        book.add_record(contact)
        message = f"✅ Contact '{name}' added."
        
    if phone:
        contact.add_phone(phone)
    return message

@logger.input_error
def remove_contact(args, book: AddressBook):
    name = args[0]
    contact = book.find_by_name(name)
    if contact:
        book.delete(name)
        return f"✅ Contact '{name}' removed."
    raise NotFoundError(f"❌ Contact '{name}' not found.")

@logger.input_error
def change_name(args, book: AddressBook):
    old_name, new_name = args
    contact = book.find_by_name(old_name)
    if contact:
        contact.edit_name(new_name)
        # Оновлюємо ключ у словнику
        book.data[new_name] = contact
        del book.data[old_name]
        return f"✅ Name updated from '{old_name}' to '{new_name}'."
    raise NotFoundError(f"❌ Contact '{old_name}' not found.")

@logger.input_error
def search_contact(args, book: AddressBook):
    query = " ".join(args)
    results = book.search(query)
    if results:
        return "\n".join(str(r) for r in results)
    return f"🔍 No contacts found matching '{query}'."

def show_all(book: AddressBook):
    if not book.data:
        return "📭 No contacts found."
    result = []
    for i, contact in enumerate(book.data.values(), 1):
        result.append(f"{i} | {contact}")
    return "\n".join(result)

# PHONE COMMANDS
@logger.input_error
def change_phone(args, book: AddressBook): # edit-phone
    name, old_number, new_number = args
    contact = book.find_by_name(name)
    if contact:
        contact.edit_phone(old_number, new_number)
        return f"✅ Phone updated for '{name}'."
    raise NotFoundError(f"❌ Contact '{name}' not found.")
    
@logger.input_error
def remove_phone(args, book: AddressBook):
    name, number = args
    contact = book.find_by_name(name)
    if contact:
        contact.remove_phone(number)
        return f"✅ Phone '{number}' removed from '{name}'."
    raise NotFoundError(f"❌ Contact '{name}' not found.")

@logger.input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    contact = book.find_by_name(name)
    if contact:
        phones = "; ".join(p.value for p in contact.phones)
        return f"📞 {name}'s phones: {phones}" if phones else f"'{name}' has no phones."
    raise KeyError

# BIRTHDAY COMMANDS
@logger.input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    contact = book.find_by_name(name)
    if contact:
        contact.add_birthday(birthday)
        return f"✅ Birthday added/updated for '{name}'."
    raise NotFoundError("❌ Contact not found.")

@logger.input_error
def remove_birthday(args, book: AddressBook):
    name = args[0]
    contact = book.find_by_name(name)
    if contact:
        contact.remove_birthday()
        return f"✅ Birthday removed for '{name}'."
    raise NotFoundError("❌ Contact not found.")

def birthdays(book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next week."
    result = ["Upcoming birthdays in next 7 days:"]
    result.extend(f"🎂 {item['name']}: {item['congratulation_date']}" for item in upcoming)
    return "\n".join(result)

# EMAIL COMMANDS
@logger.input_error
def add_email(args, book: AddressBook):
    name, email = args
    contact = book.find_by_name(name)
    if contact:
        contact.add_email(email) # Працюватиме і для change-email
        return f"✅ Email updated for '{name}'."
    raise NotFoundError("❌ Contact not found.")

@logger.input_error
def remove_email(args, book: AddressBook):
    name = args[0]
    contact = book.find_by_name(name)
    if contact:
        contact.remove_email()
        return f"✅ Email removed for '{name}'."
    raise NotFoundError("❌ Contact not found.")

# ADDRESS COMMANDS
@logger.input_error
def add_address(args, book: AddressBook):
    name = args[0]
    address = " ".join(args[1:])
    contact = book.find_by_name(name)
    if contact:
        contact.add_address(address)
        return f"✅ Address updated for '{name}'."
    raise NotFoundError("❌ Contact not found.")

@logger.input_error
def remove_address(args, book: AddressBook):
    name = args[0]
    contact = book.find_by_name(name)
    if contact:
        contact.remove_address()
        return f"✅ Address removed for '{name}'."
    raise NotFoundError("❌ Contact not found.")