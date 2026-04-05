from collections import UserDict
from datetime import datetime, timedelta
from .Record import Record

class AddressBook(UserDict):

    def add_record(self, contact: Record):
        self.data[contact.name.value] = contact
        
    def find_by_name(self, name: str) -> Record:
        record = self.data.get(name)
        if record:
            return record
        
        normalized_name = name.strip().casefold()
        for rec_name, rec in self.data.items():
            if rec_name.strip().casefold() == normalized_name:
                return rec
        return None

    def delete(self, name: str):
         if name in self.data:
            del self.data[name]
    
    # Universal search by name, email, address, phone
    def search(self, query: str) -> list:
        query = query.lower()
        results = []

        for record in self.data.values():
            contact_data = [
                str(record.name.value).lower(),
                str(record.email.value).lower() if record.email else "",
                str(record.address.value).lower() if record.address else "",
                *[p.value.lower() for p in record.phones]
            ]

            if any(query in data for data in contact_data):
                results.append(record)
        
        return results

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for contact in self.data.values():
            if contact.birthday is None:
                continue
            
            birthday = contact.birthday.value
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            days_until_birthday = (birthday_this_year - today).days

            if 0 <= days_until_birthday <= 7:
                congratulation_date = birthday_this_year
                
                weekday = congratulation_date.weekday()
                if weekday == 5:  # Saturday
                    congratulation_date += timedelta(days=2)
                elif weekday == 6:  # Sunday
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": contact.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays