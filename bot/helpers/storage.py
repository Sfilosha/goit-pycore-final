import pickle
from bot.models.AddressBook import AddressBook
from bot.models.Notebook import NoteBook

def save_contacts(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_contacts(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
    
def save_notes(book, filename="notebook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_notes(filename="notebook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NoteBook()
