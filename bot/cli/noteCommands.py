import bot.helpers.logger as logger
from bot.models.Notebook import NoteBook
from bot.models.Note import Note


@logger.input_error
def add_note(args, book: NoteBook):
    text = str(args)
    if not text or not text.strip():
        raise ValueError("❌ Note content cannot be empty.")
    new_note = Note(text)
    book.add_record(new_note)
    return f"✅ Note added successfully! (ID: {new_note.id})"

def show_all(book: NoteBook):
    if not book.data:
        return "No notes found."
    result = []
    for i, note in enumerate(book.data.values(), 1):
        result.append(f"{note}")
    return "\n".join(result)

@logger.input_error
def delete_note(args, book: NoteBook):
    text = args[0]
    noteItem = book.find(text)
    if noteItem:
        book.delete(text)
        return f"Note removed."
    return f"Note not found."