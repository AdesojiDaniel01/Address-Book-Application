import sqlite3

# Function to connect to the SQLite database
def connect():
    conn = sqlite3.connect('address_book.db')  # Connecting to the database file
    return conn

# Function to create the contacts table (if it doesn't already exist)
def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT,
            address TEXT
        );
    ''')
    conn.commit()
    conn.close()

# Function to insert a new contact into the database
def add_contact(name, phone_number, email, address):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contacts (name, phone_number, email, address)
        VALUES (?, ?, ?, ?)
    ''', (name, phone_number, email, address))
    conn.commit()
    conn.close()

# Function to view all contacts
def view_contacts():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    for contact in contacts:
        print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}, Address: {contact[4]}")
    conn.close()

# Function to update a contact's information
def update_contact(contact_id, name, phone_number, email, address):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE contacts
        SET name = ?, phone_number = ?, email = ?, address = ?
        WHERE id = ?
    ''', (name, phone_number, email, address, contact_id))
    conn.commit()
    conn.close()

# Function to delete a contact
def delete_contact(contact_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    conn.close()

# Main function to run the address book application
def main():
    create_table()  # Ensure the table exists before performing any operations

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
            print("Contact added successfully!")

        elif choice == '2':
            print("\nContacts List:")
            view_contacts()

        elif choice == '3':
            contact_id = int(input("Enter contact ID to update: "))
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            update_contact(contact_id, name, phone_number, email, address)
            print("Contact updated successfully!")

        elif choice == '4':
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
            print("Contact deleted successfully!")

        elif choice == '5':
            print("Exiting the Address Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
