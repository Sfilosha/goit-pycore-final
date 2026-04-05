def format_contact_title(r):
    # Creates unified row for console output of key user data
    name = str(r.name.value)[:15]
    
    all_phones = ", ".join(p.value for p in r.phones) if r.phones else "-"
    phones_preview = (all_phones[:17] + "..") if len(all_phones) > 19 else all_phones
    
    try:
        birthday = r.birthday.value.strftime("%d.%m.%Y") if r.birthday and r.birthday.value else "-"
    except (AttributeError, ValueError):
        birthday = str(r.birthday.value) if r.birthday else "-"
        
    email = (str(r.email.value)[:18] + "..") if r.email and len(str(r.email.value)) > 20 else (str(r.email.value) if r.email else "-")
    address = (str(r.address.value)[:18] + "..") if r.address and len(str(r.address.value)) > 20 else (str(r.address.value) if r.address else "-")

    return (
        f"👤 {name:<15} | "
        f"📞 {phones_preview:<19} | "
        f"📧 {email:<20} | "
        f"🎂 {birthday:<10} | "
        f"🏠 {address:<20}"
    )