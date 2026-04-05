from collections import UserDict
from .Note import Note

class NoteBook(UserDict):

    def add_record(self, note: Note):
        self.data[note.id] = note

    def find(self, value: str) -> Note:
        # Search by 100% text match
        return self.data.get(value)
    
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
        key_to_delete = None
        for key, note in self.data.items():
            if str(note.id) == str(id):
                key_to_delete = key
                break
        if key_to_delete:
            del self.data[key_to_delete]

    def __repr__(self):
        return f"NoteBook(total_notes={len(self.data)})"