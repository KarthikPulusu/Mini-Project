phonebook = {}

# Add contact
def add_contact():
    name = input("Enter the name: ")
    number = int(input("Enter the number: "))
    phonebook[name] = number
    print(f"Contact {name} added successfully.")

# Update contact
def update_contact():
    name = input("Enter the name: ")
    if name in phonebook:
        number = int(input("Enter the new number: "))
        phonebook[name] = number
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

# Delete contact
def delete_contact():
    name = input("Enter the name: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

# Search contact
def search_contact():
    name = input("Enter the name: ")
    if name in phonebook:
        print(f"Contact found - {name}: {phonebook[name]}")
    else:
        print(f"Contact {name} not found.")

# Print phonebook
def print_phonebook():
    if not phonebook:
        print("Phonebook is empty.")
    else:
        print("Phonebook:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")

# Main menu
while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Print Phonebook")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        print_phonebook()
    elif choice == '6':
        print("Exiting Phonebook. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
