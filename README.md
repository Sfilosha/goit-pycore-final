# 🤖 **Final Project:** Assistant Bot (CLI)

Your personal terminal assistant for managing contacts and notes. Built with Python, featuring a modern and intuitive Command Line Interface (CLI).

---

## 🌟 Key Features

### 📒 Address Book

- **Smart Addition:** Case-insensitive duplicate checking in Names ensures no redundant entries.
- **Contact Management:** Add multiple phone numbers, email, physical address, and birthday to a single record.
- **Quick Search:** Find contacts instantly using any fragment of their data.
- **Birthday Reminders:** Track upcoming birthdays for the next 7 days at a glance.

### 📝 Notebook

- **Unique Identifiers:** Each note is assigned a unique ID, allowing you to create multiple notes with identical content without conflicts.
- **Flexible Search:** Search through your notes by their unique ID or by any keyword within the text.
- **Easy Editing:** Dedicated menu-driven interface to update, modify, or delete existing notes.

### 💻 Interface

- **Interactive Navigation:** Powered by `questionary` for seamless arrow-key navigation—no more typing long commands.
- **Visual Feedback:** Color-coded status messages and hints via `colorama` for a better user experience.
- **Data Integrity:** Automatic saving ensures your data is backed up every time you exit or interrupt the program.

## 🛠 Installation

0. Clone repository

1. Create env `python3 -m venv .venv`

2. Activate enviroment (macOS) `source .venv/bin/activate` or (Windows) `.venv\Scripts\activate`

3. Install required modules `pip3 install -r requirements.txt`

4. Launch app directly from main.py `python3 main.py`

## Project Structure

- `main.py` — Entry point, main application loop, and global exception handling.

- `bot/models/` — Data logic for AddressBook, Record, NoteBook, and Note.

- `bot/cli/` — Command implementations (contactCommands.py, noteCommands.py) and UI styling.

- `bot/navigation/` — Menu configuration and sub-menu logic (menuChoices.py, subMenus.py).

- `bot/helpers/` — Utility tools for error logging and storage management.
