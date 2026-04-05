import bot.helpers.storage as storage
import bot.cli.contactCommands as contact
import bot.cli.noteCommands as note
import bot.navigation.menuChoices as menu
from bot.style import custom_style
import bot.navigation.subMenus as subMenu
import questionary
from bot.models.Record import Record


def main():
    contacts = storage.load_contacts()
    notes = storage.load_notes()
    print("Welcome to the assistant bot!")
    print("–––––––––––––––––––––––––––––––––")
    try:
        while True:
            command = questionary.select(
                "What you want to do today?",
                choices=menu.primary,
                style=custom_style,
                use_indicator=True,
                # pointer="👉"
            ).ask()

            if command is None:
                continue

            if command == "exit":
                break
            
            # CONTACTS
            elif command == "manage-contacts":
                record = subMenu.all_contacts(contacts)
                if record:
                    subMenu.manage_contact(record, contacts)

            elif command == "search":
                print(subMenu.search_contacts(contacts))

            elif command == "all-contacts":
                print(contact.show_all(contacts))

            elif command == "add-contact":
                name = questionary.text("Enter Full Name: ").ask()
                if name is None: continue
                phone = questionary.text("Enter contact phone number:").ask()
                if phone is None: continue
                result = contact.add_contact([name, phone], contacts)
                if isinstance(result, Record):
                    final_msg = subMenu.existing_contact(result, contacts, phone)
                    if final_msg: print(final_msg)
                else:
                    print(result)

            elif command == "birthdays":
                print(contact.birthdays(contacts))

            # NOTES
            elif command == "add-note":
                text = questionary.text("Enter your note: ").ask()
                if text is None: continue
                print(note.add_note(text, notes))

            elif command == "manage-notes":
                print(subMenu.manage_notes(notes))

            elif command == "all-notes":
                print(note.show_all(notes))
            
            elif command == "search-notes":
                result = subMenu.search_notes(notes)
                if result: print(result)
                
            else:
                print('Unknown command')
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
