contacts = {}
history = []

def add_contact(name, phone):
    contacts[name] = phone
    history.append((name, phone))

def view_contacts():
    names = list(contacts.keys())
    names.sort()
    for name in names:
        print(f"{name}: {contacts[name]}")

def search_contact(name):
    try:
        print(f"{name}: {contacts[name]}")
    except KeyError:
        print("Contact not found.")

def unique_phone_numbers():
    phones = set(contacts.values())
    print("Unique phone numbers:", phones)

# Example usage:
add_contact("Alice", "1234567890")
add_contact("Bob", "0987654321")
view_contacts()
search_contact("Alice")
search_contact("Charlie")
unique_phone_numbers()
print("Contact history:", history)
