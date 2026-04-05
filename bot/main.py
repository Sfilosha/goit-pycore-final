import bot.helpers.storage as storage
import bot.cli.contactCommands as contact
import bot.cli.noteCommands as note
import bot.cli.tagCommands as tag
from bot.helpers.parse_input import parse_input
from bot.helpers.help_commands import help_commands


def main():
    contacts = storage.load_contacts()
    notes = storage.load_notes()
    print("Welcome to the assistant bot!")
    print("–––––––––––––––––––––––––––––––––")
    try:
        while True:
            user_input = input("Enter a command: ")
            if not user_input.strip():
                continue
            
            command, *args = parse_input(user_input)

            if command is None:
                continue

            if command in ["exit", "close"]:
                break
            
            # --- CONTACTS ---
            elif command == "add-contact":
                # Usage: add-contact [name] [phone (optional)]
                # Example: add-contact John 0987654321
                print(contact.add_contact(args, contacts))

            elif command == "delete-contact":
                # Usage: delete-contact [name]
                # Example: delete-contact John
                print(contact.remove_contact(args, contacts))

            elif command == "search-contact":
                # Usage: search-contact [query]
                # Example: search-contact Joh
                print(contact.search_contact(args, contacts))

            elif command == "all-contacts":
                # Usage: all-contacts
                print(contact.show_all(contacts))

            elif command == "birthdays":
                # Usage: birthdays
                print(contact.birthdays(contacts))

            elif command == "change-name":
                # Usage: change-name [old_name] [new_name]
                # Example: change-name John Johnny
                print(contact.change_name(args, contacts))

            # --- PHONE ---
            elif command == "remove-phone":
                # Usage: remove-phone [name] [phone]
                # Example: remove-phone John 0987654321
                print(contact.remove_phone(args, contacts))

            elif command == "show-phone":
                # Usage: show-phone [name]
                # Example: show-phone John
                print(contact.show_phone(args, contacts))
            
            elif command == "edit-phone":
                # Usage: edit-phone [name] [old_phone] [new_phone]
                # Example: edit-phone John 0987654321 0123456789
                print(contact.change_phone(args, contacts))
            
            # --- BIRTHDAY ---
            elif command in ["add-birthday", "change-birthday"]:
                # Usage: add-birthday [name] [DD.MM.YYYY]
                # Example: add-birthday John 25.12.1990
                print(contact.add_birthday(args, contacts))
                
            elif command == "remove-birthday":
                # Usage: remove-birthday [name]
                # Example: remove-birthday John
                print(contact.remove_birthday(args, contacts))
            
            # --- EMAIL ---
            elif command in ["add-email", "change-email"]:
                # Usage: add-email [name] [email]
                # Example: add-email John john@example.com
                print(contact.add_email(args, contacts))
                
            elif command == "remove-email":
                # Usage: remove-email [name]
                # Example: remove-email John
                print(contact.remove_email(args, contacts))

            # --- ADDRESS ---
            elif command in ["add-address", "change-address"]:
                # Usage: add-address [name] [address text...]
                # Example: add-address John 123 Main St, Apt 4B
                print(contact.add_address(args, contacts))
                
            elif command == "remove-address":
                # Usage: remove-address [name]
                # Example: remove-address John
                print(contact.remove_address(args, contacts))
            
            # --- TAGS ---
            elif command == "add-tag":
                # Usage: add-tag [name] [tag1] [tag2] ...
                # Example: add-tag John work python designer
                print(tag.add_tag(args, contacts))

            elif command == "remove-tag":
                # Usage: remove-tag [name] [tag]
                # Example: remove-tag John python
                print(tag.remove_tag(args, contacts))

            elif command == "search-tag":
                # Usage: search-tag [tag]
                # Example: search-tag python
                print(tag.search_by_tag(args, contacts))

            # --- NOTES ---
            elif command == "add-note":
                # Usage: add-note [text...]
                # Example: add-note Buy milk and eggs
                print(note.add_note(args, notes))

            elif command == "all-notes":
                # Usage: all-notes
                print(note.show_all(notes))
            
            elif command == "search-notes":
                # Usage: search-notes [query]
                # Example: search-notes milk
                print(note.search_notes(args, notes))

            elif command == "delete-note":
                # Usage: delete-note [id]
                # Example: delete-note a1b2
                print(note.delete_note(args, notes))
                
            elif command == "edit-note":
                # Usage: edit-note [id] [new text...]
                # Example: edit-note a1b2 Buy milk, eggs, and bread
                print(note.edit_note(args, notes))

            elif command == "help":
                print(help_commands())
                
            else:
                print("Invalid command. Enter 'help' to see all commands.")
                
    except KeyboardInterrupt:
        print("\n⚠️  Program interrupted! Saving data before exit...")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        storage.save_contacts(contacts)
        storage.save_notes(notes)
        print("💾 All data saved successfully. Goodbye!")

if __name__ == "__main__":
    main()
