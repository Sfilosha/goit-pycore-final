import questionary
from bot.helpers.logger import input_error
from questionary import Choice, Separator
from bot.models.Note import Note
from bot.models.AddressBook import AddressBook
from bot.models.Notebook import NoteBook
from bot.models.Record import Record
import bot.cli.contactCommands as contactCmd
from bot.style import custom_style
from bot.helpers.contactDetails import contact_details, phones_details
from bot.helpers.formatContactDetails import format_contact_title
from bot.navigation.menuChoices import edit_contact
from bot.models.Errors import NotFoundError


@input_error
def all_contacts(contacts):
    if not contacts.data:
        print("📭 Address book is empty.")
        return None
    choices = [
            Choice(title="⬅️ Back", value="back"),
            Separator("⎯" * 20)
    ]
    choices.extend([
        Choice(title=format_contact_title(record), value=record)
        for record in contacts.data.values()
    ])

    selected = questionary.select(
        "Select a contact to manage:",
        choices=choices,
        style=custom_style,
        pointer="🔍",
    ).ask()

    return selected if selected != "back" else None

@input_error
def manage_contact(record, book: AddressBook):
    while True:
        cmd = questionary.select(
            contact_details(record),
            style=custom_style,
            choices=edit_contact,
        ).ask()

        if cmd == "exit" or cmd is None:
            break

        if cmd == "name":
            new_name = questionary.text("Enter new name:", default=record.name.value).ask()
            print(contactCmd.edit_contact_name(record, new_name))
        
        if cmd == "phone":
            edit_phone(record)

        elif cmd == "email":
            uni_edit(
                "Email", 
                record.email.value if record.email else None, 
                record.add_email, 
                record.remove_email
            )

        elif cmd == "address":
            uni_edit(
                "Address", 
                record.address.value if record.address else None, 
                record.add_address, 
                record.remove_address
            )

        elif cmd == "birthday":
            current_val = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else None
            uni_edit(
                "Birthday", 
                current_val, 
                record.add_birthday, 
                record.remove_birthday
            )


        elif cmd == "delete":
            confirm = questionary.confirm(f"Are you sure you want to delete {record.name.value}?").ask()
            if confirm:
                print(contactCmd.delete_contact(record, book))
                break

@input_error
def edit_phone(record):
    while True:
        choices = [
            Choice(title="⬅️ Back", value="back"),
            Separator("⎯" * 20)
        ]
        
        if record.phones:
            for phone in record.phones:
                choices.append(Choice(title=f"📞 {phone.value}", value=phone))
        
        choices.append(Separator("⎯" * 20))
        choices.append(Choice(title="➕ Add new number", value="add"))

        selected = questionary.select(
            phones_details(record),
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "back" or selected is None:
            break

        if selected == "add":
            print(contactCmd.add_phone(record))
        
        else:
            phones(record, selected)

@input_error
def phones(record, phone: object):
    while True:
        action = questionary.select(
            f"Action for {phone.value}:",
            style=custom_style,
            choices=[
                Choice(title="✏️ Edit", value="edit"),
                Choice(title="🗑️ Delete", value="delete"),
                Choice(title="⬅️ Back", value="back")
            ]
        ).ask()

        if action == "back" or action is None:
            break

        if action == "edit":
            new_val = questionary.text("Enter updated phone:", default=phone.value).ask()
            if new_val:
                print(contactCmd.edit_phone(record, phone, new_val))

        elif action == "delete":
            confirm = questionary.confirm(f"Are you sure you want to delete {phone.value}?").ask()
            if confirm:
                print(contactCmd.delete_phone(record, phone))
                break

@input_error
def flow_edit_note(note: Note):
    print(f"\n📝 Editing Note ID: {note.id}")
    print(f"Created at: {note.createdAt.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 20)

    updated_text = questionary.text(
        "Update your note:",
        default=note.text.value
    ).ask()

    if updated_text is not None and updated_text != note.text.value:
        note.edit(updated_text)
        return f"✅ Note updated successfully!"
    else:
        return f"ℹ️ No changes made."

@input_error
def manage_notes(notebook: NoteBook):
    while True:
        if not notebook.data:
            print("📭 Your notebook is empty.")
            return
        
        choices = [
            Choice(title="⬅️ Back", value="back"),
            Separator("⎯" * 20)
        ]
        choices.extend(
            Choice(title=f"[{n.id}] {str(n.text.value)[:50]}...", value=n) 
            for n in notebook.data.values()
        )    

        selected_note = questionary.select("Select a note to manage:", choices=choices).ask()

        if selected_note == "back" or selected_note is None:
            break
        
        uni_edit(
            field_name="Note",
            current_value=selected_note.text.value,
            update_func=selected_note.edit,
            remove_func=lambda: notebook.delete(selected_note.id)
        )

def uni_edit(field_name, current_value, update_func, remove_func):
    if not current_value:
        new_val = questionary.text(f"Enter {field_name.lower()}:").ask()
        if new_val and new_val.strip():
            update_func(new_val)
            return f"✅ {field_name} added!"
        return

    action = questionary.select(
        f"{field_name} actions (Current: {current_value if current_value else 'Empty'}):",
        style=custom_style,
        choices=[
            Choice(title="✏️ Edit / Add", value="edit"),
            Choice(title="🗑️ Remove", value="delete"),
            Choice(title="⬅️ Back", value="back")
        ]
    ).ask()

    if action == "edit":
        new_val = questionary.text(f"Enter {field_name.lower()}:", default=str(current_value) if current_value else "").ask()
        if new_val and new_val.strip():
            update_func(new_val)
            return f"✅ {field_name} updated!"
            
    elif action == "delete":
        if current_value:
            if questionary.confirm(f"Are you sure you want to remove {field_name.lower()}?").ask():
                remove_func()
                return f"🗑️ {field_name} removed!"
        else:
            return f"ℹ️ {field_name} is already empty."

@input_error
def search_contacts(book: AddressBook):
    query = questionary.text("🔍 Enter search query (name, phone, email, etc.):").ask()
    
    if not query or not query.strip():
        return

    found_contacts = book.search(query)

    if not found_contacts:
        raise NotFoundError("❌ No contacts found for '{query}'.")
        

    choices = [
        Choice(title="⬅️ Back", value="back"),
        Separator("⎯" * 100)
    ]

    choices.extend([
        Choice(title=format_contact_title(r), value=r)
        for r in found_contacts
    ])

    selected = questionary.select(
        f"Found {len(found_contacts)} results. Select to manage:",
        choices=choices,
        style=custom_style,
        pointer="🔍"
    ).ask()

    if selected and selected != "back":
        manage_contact(selected, book)

@input_error
def existing_contact(existing_record, book, phone):
    print(f"⚠️  Contact '{existing_record.name.value}' already exists.")
    
    choice = questionary.select(
        "How to proceed?",
        style=custom_style,
        choices=[
            Choice(title=f"➕ Add to: {format_contact_title(existing_record)}", value="append"),
            Choice(title="🆕 Create new entry", value="new"),
            Choice(title="⬅️  Cancel", value="cancel")
        ], 
    ).ask()

    if choice == "append":
        return contactCmd.append_phone_to_existing(existing_record, phone)
    
    elif choice == "new":
        new_name = questionary.text("Enter unique name:").ask()
        if new_name:
            result = contactCmd.add_contact([new_name, phone], book)
            if isinstance(result, Record):
                return existing_contact(result, book, phone)
            return result
            
    return "❌ Operation cancelled."

@input_error
def search_notes(notebook: NoteBook):
    query = questionary.text("🔍 Enter search query (ID or text content):").ask()
    
    if not query or not query.strip():
        return "❌ Search cancelled."
    
    while True:

        found_notes = notebook.search(query)

        if not found_notes:
            return NotFoundError("❌ No notes found matching '{query}'.")

        choices = [
            Choice(title="⬅️ Back", value="back"),
            Separator("⎯" * 40)
        ]

        choices.extend([
            Choice(
                title=f"[{n.id}] {str(n.text.value)[:50]}...", 
                value=n
            )
            for n in found_notes
        ])

        selected = questionary.select(
            f"Found {len(found_notes)} notes. Select to manage:",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "back" or selected is None:
            break

        uni_edit(
            field_name="Note",
            current_value=selected.text.value,
            update_func=selected.edit,
            remove_func=lambda: notebook.delete(selected.id)
        )
        
    return "✅ Search completed."