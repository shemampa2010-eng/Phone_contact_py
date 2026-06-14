def add_contact():
    name = input ("Nom et prenom: ")
    phone = input("Numero de tel: ")
    email = input ("Email: ")
    contacts.append ({
        "name": name,
        "phone": phone,
        "email": email
      })

    print ("New contact added: \n" , contacts)

def remove_contact():
    target_contact = input ("Name of the contact you want to delete: ")
    for contact in contacts :
        if contact["name"] == target_contact :
            contacts.remove (contact)
            print ("Contact", target_contact , "has been removed")    

def review_contact():
    print ("---Contact list---\n" , contacts)



contacts = []

while True :
    operation = input ("Which operation do you want to do ? ""\n 1: To review a contact" "\n 2: To add a contact" "\n 3: To delete a contact " "\n operation number: " )
    if operation == "2" :
        add_contact()
    elif operation == "1":
        review_contact()
    elif operation == "3":
        remove_contact()   
    else :
        print ("--Operation invalid--\n")
        