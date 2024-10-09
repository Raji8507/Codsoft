import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_name TEXT,
    phone_number TEXT,
    email TEXT,
    address TEXT
)
""")
conn.commit()


def add_contact():
    store_name = entry_store_name.get()
    phone_number = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if store_name and phone_number:
        cursor.execute("""
        INSERT INTO contacts (store_name, phone_number, email, address)
        VALUES (?, ?, ?, ?)""", (store_name, phone_number, email, address))
        conn.commit()
        messagebox.showinfo("Success", "Contact added!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Store name and phone number are required")

def view_contacts():
    listbox_contacts.delete(0, tk.END)
    cursor.execute("SELECT store_name, phone_number FROM contacts")
    contacts = cursor.fetchall()
    for contact in contacts:
        listbox_contacts.insert(tk.END, contact)

def search_contact():
    search_term = entry_search.get()
    listbox_contacts.delete(0, tk.END)
    cursor.execute("SELECT store_name, phone_number FROM contacts WHERE store_name LIKE ? OR phone_number LIKE ?", 
                   ('%' + search_term + '%', '%' + search_term + '%'))
    contacts = cursor.fetchall()
    for contact in contacts:
        listbox_contacts.insert(tk.END, contact)

def delete_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    store_name = selected_contact[0]
    cursor.execute("DELETE FROM contacts WHERE store_name=?", (store_name,))
    conn.commit()
    messagebox.showinfo("Success", "Contact deleted")
    view_contacts()

def update_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    store_name = selected_contact[0]
    new_phone = entry_phone.get()
    new_email = entry_email.get()
    new_address = entry_address.get()

    cursor.execute("""
    UPDATE contacts
    SET phone_number = ?, email = ?, address = ?
    WHERE store_name = ?
    """, (new_phone, new_email, new_address, store_name))
    conn.commit()
    messagebox.showinfo("Success", "Contact updated")
    clear_entries()
    view_contacts()

def clear_entries():
    entry_store_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Manager")

# Labels and Entry Fields
tk.Label(root, text="Store Name:").grid(row=0, column=0)
entry_store_name = tk.Entry(root)
entry_store_name.grid(row=0, column=1)

tk.Label(root, text="Phone Number:").grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

tk.Label(root, text="Address:").grid(row=3, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1)

# Buttons
btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.grid(row=4, column=0)

btn_update = tk.Button(root, text="Update Contact", command=update_contact)
btn_update.grid(row=4, column=1)

btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=5, column=0)

tk.Label(root, text="Search:").grid(row=6, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=6, column=1)
btn_search = tk.Button(root, text="Search", command=search_contact)
btn_search.grid(row=6, column=2)

listbox_contacts = tk.Listbox(root, width=50, height=10)
listbox_contacts.grid(row=7, column=0, columnspan=3)

btn_view = tk.Button(root, text="View All Contacts", command=view_contacts)
btn_view.grid(row=8, column=0, columnspan=3)

view_contacts()
root.mainloop()
