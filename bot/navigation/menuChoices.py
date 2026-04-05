from questionary import Separator, Choice

separatorWidth = 20

primary = [
    # Contacts Commands
    # Separator("== CHOOSE ACTION =="),
    Choice(title="See All Contacts", value="all-contacts"),
    Choice(title="Add New Contact", value="add-contact"),
    Choice(title="Manage Contacts", value="manage-contacts"),
    Choice(title="Search Contact", value="search"),
    Choice(title="See Upcoming Birthdays", value="birthdays"),

    Separator("" + "—" * separatorWidth),
    
    # Notes Commands
    Choice(title="See All Notes", value="all-notes"),
    Choice(title="Add Note", value="add-note"),
    Choice(title="Manage Notes", value="manage-notes"),
    Choice(title="Search Note", value="search-notes"),
    Separator("" + "—" * separatorWidth),
    
    # System Commands
    Choice(title="Close program", value="exit"),
]

edit_contact = [
    Choice(title="⬅️ Back", value="exit"),
    Separator("⎯" * separatorWidth),
    Choice(title="✏️ Edit Name", value="name"),
    Choice(title="📞 Edit Phones", value="phone"), 
    Choice(title="📧 Edit Email", value="email"), 
    Choice(title="🏠 Edit Address", value="address"), 
    Choice(title="🎂 Set Birthday", value="birthday"), 
    Separator("⎯" * separatorWidth),
    Choice(title="⛔️ Delete Contact", value="delete"),
]

edit_note = [
    Choice(title="⬅️ Back", value="exit"),
    Separator("⎯" * separatorWidth),
    Choice(title="✏️ Edit Content", value="edit"),
    Choice(title="⛔️ Delete Note", value="delete"),
]