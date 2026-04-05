import bot.helpers.logger as logger
from bot.models.Notebook import NoteBook
from bot.models.Note import Note
from bot.models.Errors import NotFoundError

@logger.input_error
def add_note(args, book: NoteBook):
    text = " ".join(args)
    if not text or not text.strip():
        raise ValueError("❌ Note content cannot be empty.")
    new_note = Note(text)
    book.add_record(new_note)
    return f"✅ Note added successfully! (ID: {new_note.id})"

def show_all(book: NoteBook):
    if not book.data:
        return "📭 No notes found."
    result = [str(note) for note in book.data.values()]
    return "\n".join(result)

@logger.input_error
def search_notes(args, book: NoteBook):
    query = " ".join(args)
    results = book.search(query)
    if results:
        return "\n".join(str(n) for n in results)
    return f"🔍 No notes found matching '{query}'."

@logger.input_error
def delete_note(args, book: NoteBook):
    note_id = args[0]
    note = book.find_by_id(note_id)
    if note:
        book.delete(note_id)
        return f"🗑️ Note {note_id} removed."
    raise NotFoundError(f"❌ Note {note_id} not found.")

@logger.input_error
def edit_note(args, book: NoteBook):
    if len(args) < 2:
        raise ValueError("❌ Usage: edit-note [id] [new text]")
    note_id = args[0]
    new_text = " ".join(args[1:])
    note = book.find_by_id(note_id)
    if note:
        note.edit(new_text)
        return f"✅ Note {note_id} updated."
    raise NotFoundError(f"❌ Note {note_id} not found.")