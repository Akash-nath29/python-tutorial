

# Function to display all contacts
def display_contacts():
    if contacts:
        print("Contacts List:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")

# Function to search for a contact by name
def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

# Main loop
def contact_manager():
    while True:
        print("\n1. Add Contact\n2. Display Contacts\n3. Delete Contact\n4. Search Contact\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to search: ")
            search_contact(name)
        elif choice == '5':
            print("Exiting contact manager.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the contact manager
contact_manager()
