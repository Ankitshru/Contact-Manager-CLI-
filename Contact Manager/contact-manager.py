import json


def load_data():
    try:
        with open("contact.txt", "r") as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading the contact file. It may be corrupted.")
        return []

def save_data(contact):
    with open("contact.txt", "w") as file:
        json.dump(contact, file)


#Add Contact
def add_contact(contact):
    name = input("Enter the name: ")
    number = input("Enter contact number: ")

    contact.append({'name': name, 'number': number})
    save_data(contact)


#Update the existing contact
def update_contact(contact):    
    index = int(input("Enter the index of the contact you want to update: "))
    if index < 0 or index >= len(contact):
        name = input("Enter the name of the contact you want to update: ")
        number = input("Enter the new contact number: ")
        
        contact[index-1] = {'name': name, 'number': number}
        save_data(contact)
    else:
        print("Invalid index number")
    print("Contact updated successfully.")


#Searches the contact by either name or number
def search_contact(contact):
    search_contact = input("Enter the name or number you want to search: ")
    with open("contact.txt", "r") as file:
        contacts = json.load(file)
        found_contacts = [contact for contact in contacts if search_contact in contact['name'] or search_contact in contact['number']]
    print("Here is your contact you have searched", found_contacts)

#shows all contact details
def view_all_contact(contact):
    print("Here all the contact")
    for index, item in enumerate(contact, start=1):
        print(f"{index}. Name: {item['name']}, Number: {item['number']}")

# delete contact 
def delete_contact(contact):
    index = int(input("Enter the index of the contact you want to delete: "))
    if index < 0 or index >= len(contact):
        del contact[index-1]
        save_data(contact)

    else:
        print("Invalid index number")
    print("Contact deleted successfully.")

def main():
    contacts = load_data()
    while True:
        print("\n Your Contact Book")
        print("1. View all contact ")
        print("2. Add New Contact ")
        print("3 Search Contact ")
        print("4. Update Contact details ")
        print("5. Delete a contact ")
        print("6. Exit the App")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                view_all_contact(contacts)
            case "2":
                add_contact(contacts)
            case "3":
                search_contact(contacts)
            case "4":
                update_contact(contacts)
            case "5":
                delete_contact(contacts)
            case "6":
                break
            case _:
                print("Invalid choice")
            

if __name__ == "__main__":
    main()