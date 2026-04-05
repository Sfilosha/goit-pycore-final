def help_commands():
    return ("""
                    🤖 Available Commands:

                    --- CONTACTS ---
                    add-contact [name] [phone]       : Add a new contact or add phone to existing.
                    delete-contact [name]            : Delete a contact.
                    search-contact [query]           : Search contacts by name, phone, email, etc.
                    all-contacts                     : Show all contacts.
                    change-name [old] [new]          : Change a contact's name.

                    --- PHONES ---
                    show-phone [name]                : Show phones for a contact.
                    edit-phone [name] [old] [new]    : Change a specific phone number.
                    remove-phone [name] [phone]      : Remove a specific phone number.

                    --- BIRTHDAYS ---
                    add-birthday [name] [DD.MM.YYYY] : Add or update a birthday (e.g., 25.12.1990).
                    remove-birthday [name]           : Remove a birthday.
                    birthdays                        : Show upcoming birthdays for the next 7 days.

                    --- EMAILS & ADDRESSES ---
                    add-email [name] [email]         : Add or update an email.
                    remove-email [name]              : Remove an email.
                    add-address [name] [address...]  : Add or update an address.
                    remove-address [name]            : Remove an address.

                    --- TAGS ---
                    add-tag [name] [tag1] [tag2]...  : Add one or more tags to a contact.
                    remove-tag [name] [tag]          : Remove a specific tag.
                    search-tag [tag]                 : Find contacts by tag.

                    --- NOTES ---
                    add-note [text...]               : Create a new note.
                    all-notes                        : Show all notes.
                    search-notes [query]             : Search notes by ID or content.
                    edit-note [id] [new text...]     : Edit an existing note.
                    delete-note [id]                 : Delete a note by its ID.

                    --- SYSTEM ---
                    help                             : Show this message.
                    exit / close                     : Save data and exit the program.
                    """)