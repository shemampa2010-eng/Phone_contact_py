def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    return contact

def remove_contact(contacts, target_contact):
    for contact in contacts:
        if contact["name"] == target_contact:
            contacts.remove(contact)
            print("Contact", target_contact, "has been removed")

def review_contact(contacts):
    print("---Contact list---\n", contacts)

def count_contact(contacts):
    print("Total contact", len(contacts))

contacts = []

while True:
    operation = input(
        "Which operation do you want to do ?"
        "\n 1: To review a contact"
        "\n 2: To add a contact"
        "\n 3: To delete a contact"
        "\n 4: To quit"
        "\n operation number: "
    )

    if operation == "2":
        name = input("Nom et prenom: ")
        phone = input("Numero de tel: ")
        email = input("Email: ")

        contacts.append(add_contact(name, phone, email))
        print("New contact added")

    elif operation == "1":
        review_contact(contacts)

    elif operation == "3":
        target_contact = input("Name of the contact you want to delete: ")
        remove_contact(contacts, target_contact)

    elif operation == "4":
        break

    else:
        print("--Operation invalid--\n")