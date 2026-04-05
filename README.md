# 🤖 Final Project: Assistant Bot (CLI) - Simple

Your personal terminal assistant for managing contacts and notes. Built with Python, featuring a blazing-fast, linear Command Line Interface (CLI) designed for power users.

---

## 🌟 Key Features

### 📒 Address Book

- **Smart Addition:** Case-insensitive duplicate checking ensures no redundant entries.
- **Rich Contact Management:** Add multiple phone numbers, emails, physical addresses, and birthdays to a single record.
- **🏷️ Tagging System:** Organize contacts with custom tags (e.g., `#work`, `#python`) and find them instantly.
- **Quick Search:** Find contacts using any fragment of their data (name, phone, email, tags, etc.).
- **Birthday Reminders:** Track upcoming birthdays for the next 7 days at a glance.

### 📝 Notebook

- **Unique Identifiers:** Each note is assigned a unique short ID (e.g., `a1b2`), allowing you to create multiple notes with identical content without conflicts.
- **Flexible Search:** Search through your notes by their unique ID or by any keyword within the text.
- **Fast Editing:** Quickly update or delete notes directly via command arguments.

### 💻 Interface & Under the Hood

- **Lightning Fast CLI:** Pure linear command execution. Type what you need and get instant results.
- **Built-in Help:** Instantly view all available commands and usage examples via the `help` command.
- **Visual Feedback:** Color-coded status messages and error handling via `colorama` for a smooth user experience.
- **Data Integrity:** Automatic saving ensures your data is backed up safely every time you exit or interrupt the program.

---

## 🛠 Installation & Setup

0. Clone the repository
1. Create a virtual environment: `python3 -m venv .venv`
2. Activate the environment:
   - macOS/Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
3. Install required modules: `pip3 install -r requirements.txt`
4. Launch the app: `python3 main.py`
5. _(Optional)_ Run the automated test suite: `python3 test_commands.py`

---

## 🚀 Quick Start Example

Launch the app and try these commands:

```bash
>>> add-contact "John Smith" 0987654321
✅ Contact 'John Smith' added.

>>> add-tag "John Smith" python developer
✅ Tags #python, #developer added to 'John Smith'.

>>> add-note Lorem dolom ipsur
✅ Note added successfully! (ID: x7y9)

>>> help
🤖 Available Commands: ...
```

## Project Structure

- `main.py` — Entry point, main application loop, and global exception handling.

- `bot/models/` — Data logic for AddressBook, Record, NoteBook, and Note.

- `bot/cli/` — Command implementations (contactCommands.py, noteCommands.py, tagCommands.py).

- `bot/helpers/` — Utility tools for error logging and storage management.
