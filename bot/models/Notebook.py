from collections import UserDict
from .Note import Note

class NoteBook(UserDict):

    def add_record(self, note: Note):
        self.data[note.id] = note

    def find_by_id(self, note_id: str) -> Note:
        for key, note in self.data.items():
            if str(key) == str(note_id):
                return note
        return None
    
    def search(self, query: str) -> list:
        # Search by id and text
        query = query.lower()
        results = []

        for note in self.data.values():
            id_match = query in str(note.id).lower()
            text_match = query in note.text.value.lower()

            if id_match or text_match:
                results.append(note)
        
        return results

    def delete(self, id: str):
        if id in self.data:
            del self.data[id]

    def __repr__(self):
        return f"NoteBook(total_notes={len(self.data)})"