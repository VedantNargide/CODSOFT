import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

class ContactInformation:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Information")
        self.root.geometry("500x600")

        # Create frames
        self.frame_add = tk.Frame(self.root)
        self.frame_add.pack(fill="x")

        self.frame_search = tk.Frame(self.root)
        self.frame_search.pack(fill="x")

        self.frame_view = tk.Frame(self.root)
        self.frame_view.pack(fill="both", expand=True)

        # Create input fields
        self.name_label = tk.Label(self.frame_add, text="Name:")
        self.name_label.pack(side="left", padx=10, pady=10)

        self.name_entry = tk.Entry(self.frame_add, width=20)
        self.name_entry.pack(side="left", padx=10, pady=10)

        self.phone_label = tk.Label(self.frame_add, text="Phone:")
        self.phone_label.pack(side="left", padx=10, pady=10)

        self.phone_entry = tk.Entry(self.frame_add, width=20)
        self.phone_entry.pack(side="left", padx=10, pady=10)

        self.email_label = tk.Label(self.frame_add, text="Email:")
        self.email_label.pack(side="left", padx=10, pady=10)

        self.email_entry = tk.Entry(self.frame_add, width=20)
        self.email_entry.pack(side="left", padx=10, pady=10)

        self.address_label = tk.Label(self.frame_add, text="Address:")
        self.address_label.pack(side="left", padx=10, pady=10)

        self.address_entry = tk.Entry(self.frame_add, width=20)
        self.address_entry.pack(side="left", padx=10, pady=10)

        # Create add data button
        self.add_button = tk.Button(self.frame_add, text="Add Data", command=self.add_data)
        self.add_button.pack(side="right", padx=10, pady=10)

        # Create search functionality
        self.search_label = tk.Label(self.frame_search, text="Search:")
        self.search_label.pack(side="left", padx=10, pady=10)

        self.search_entry = tk.Entry(self.frame_search, width=20)
        self.search_entry.pack(side="left", padx=10, pady=10)

        self.search_button = tk.Button(self.frame_search, text="Search", command=self.search_data)
        self.search_button.pack(side="left", padx=10, pady=10)

        self.update_button = tk.Button(self.frame_search, text="Update", command=self.update_data)
        self.update_button.pack(side="left", padx=10, pady=10)

        self.delete_button = tk.Button(self.frame_search, text="Delete", command=self.delete_data)
        self.delete_button.pack(side="left", padx=10, pady=10)

        # Create table view
        self.treeview = ttk.Treeview(self.frame_view, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.treeview.pack(fill="both", expand=True)

        self.treeview.heading("Name", text="Name")
        self.treeview.heading("Phone", text="Phone")
        self.treeview.heading("Email", text="Email")
        self.treeview.heading("Address", text="Address")

        # Initialize data storage
        self.contacts = []

    def add_data(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not all([name, phone, email, address]):
            messagebox.showerror("Error", "All fields are mandatory")
            return

        if not self.validate_phone(phone):
            messagebox.showerror("Error", "Invalid mobile number")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format")
            return

        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        self.display_data()
        self.clear_fields()

    def validate_phone(self, phone):
        pattern = re.compile(r"^(86|98|70|93|94|75)\d{8}$")
        if pattern.match(phone):
            return True
        return False

    def validate_email(self, email):
        pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if pattern.match(email):
            return True
        return False

    def search_data(self):
        search_term = self.search_entry.get()
        results = [contact for contact in self.contacts if search_term in contact["name"] or search_term in contact["phone"] or search_term in contact["email"] or search_term in contact["address"]]
        self.display_data(results)

    def update_data(self):
        selected_row = self.treeview.selection()[0]
        index = self.treeview.index(selected_row)
        contact = self.contacts[index]
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, contact["name"])
        self.phone_entry.delete(0, "end")
        self.phone_entry.insert(0, contact["phone"])
        self.email_entry.delete(0, "end")
        self.email_entry.insert(0, contact["email"])
        self.address_entry.delete(0, "end")
        self.address_entry.insert(0, contact["address"])
        self.add_button.config(text="Update Data", command=lambda: self.update_contact(index))

        

    def update_contact(self, index):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not all([name, phone, email, address]):
            messagebox.showerror("Error", "All fields are mandatory")
            return

        if not self.validate_phone(phone):
            messagebox.showerror("Error", "Invalid mobile number")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format")
            return

        if not all([name, phone, email, address]):
            messagebox.showerror("Error", "All fields are mandatory")
            return

        self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
        self.display_data()
        self.clear_fields()
        self.add_button.config(text="Add Data", command=self.add_data)

        

    def delete_data(self):
        selected_row = self.treeview.selection()[0]
        index = self.treeview.index(selected_row)
        confirm = messagebox.askyesno("Confirm", "Do you want to delete the selected data?")
        if confirm:
            self.treeview.delete(selected_row)
            del self.contacts[index]

    def display_data(self, data=None):
        if data is None:
            data = self.contacts

        self.treeview.delete(*self.treeview.get_children())
        for i, contact in enumerate(data, 1):
            self.treeview.insert("", "end", values=(contact["name"], contact["phone"], contact["email"], contact["address"]))
            self.treeview.column("#0", width=0, stretch="no")
            self.treeview.column("Name", anchor="center", width=100)
            self.treeview.column("Phone", anchor="center", width=100)
            self.treeview.column("Email", anchor="center", width=100)
            self.treeview.column("Address", anchor="center", width=100)

    def clear_fields(self):
        self.name_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.address_entry.delete(0, "end")
        self.add_button.config(text="Add Data")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactInformation(root)
    root.mainloop()