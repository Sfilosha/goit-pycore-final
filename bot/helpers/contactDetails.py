def contact_details(record): 
    return (
    f"\n"
    f"👤 Name:     {record.name.value}\n"
    f"📞 Phones:   {', '.join(p.value for p in record.phones) if record.phones else 'No phones'}\n"
    f"📧 Email:    {record.email.value if record.email else 'Empty'}\n"
    f"🏠 Address:  {record.address.value if record.address else 'Empty'}\n"
    f"🎂 Birthday: {record.birthday.value.strftime("%d.%m.%Y") if record.birthday else 'Empty'}\n"
    f"{'—' * 20}\n"
    f"What would you like to do?"
    )

def phones_details(record): 
    return (
    f"Manage Contact Phones \n"
    f"👤 Name:     {record.name.value}\n"
    f"What would you like to do?"
    )