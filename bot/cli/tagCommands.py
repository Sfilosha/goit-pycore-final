import bot.helpers.logger as logger
from bot.models.AddressBook import AddressBook
from bot.models.Errors import NotFoundError

@logger.input_error
def add_tag(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("❌ Usage: add-tag [contact_name] [tag1] [tag2] ...")
    
    name = args[0]
    tags_to_add = args[1:]
    contact = book.find_by_name(name)
    
    if contact:
        added = []
        for tag_str in tags_to_add:
            try:
                contact.add_tag(tag_str)
                added.append(f"#{tag_str.lower()}")
            except ValueError:
                pass
                
        if added:
            return f"✅ Tags {', '.join(added)} added to '{name}'."
        return f"ℹ️ No new tags were added (maybe they already exist)."
    raise NotFoundError(f"❌ Contact '{name}' not found.")

@logger.input_error
def remove_tag(args, book: AddressBook):
    if len(args) < 2:
         raise ValueError("❌ Usage: remove-tag [contact_name] [tag]")
    
    name, tag_str = args
    contact = book.find_by_name(name)
    if contact:
        contact.remove_tag(tag_str)
        return f"✅ Tag '#{tag_str.lower()}' removed from '{name}'."
    raise NotFoundError(f"❌ Contact '{name}' not found.")

@logger.input_error
def search_by_tag(args, book: AddressBook):
    if not args:
         raise ValueError("❌ Usage: search-tag [tag]")
    
    tag_query = args[0].strip().lower()
    if tag_query.startswith('#'):
        tag_query = tag_query[1:]
        
    results = []
    for record in book.data.values():
        if any(t.value == tag_query for t in record.tags):
            results.append(record)

    if results:
        return f"🔍 Contacts with tag '#{tag_query}':\n" + "\n".join(str(r) for r in results)
    return f"🔍 No contacts found with tag '#{tag_query}'."