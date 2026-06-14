# Phone_contact

A simple Python command-line contact manager that allows you to store, view, and delete contacts.


---

## Features

- Add a new contact (name, phone, email)
- View all saved contacts
- Delete a contact by name
- Runs in an interactive loop until you exit

---

## How it works

Contacts are stored in a Python list of dictionaries.

Each contact looks like this:

```python
{
  "name": "John Doe",
  "phone": "123456789",
  "email": "john@mail.com"
}
