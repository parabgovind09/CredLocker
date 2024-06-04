import tkinter as tk
from tkinter import messagebox
import re
import MergeAdmin

def submit_form():
    try:
        institution_name = entry_institution_name.get().strip()
        address = entry_address.get().strip()
        contact1 = entry_contact1.get().strip()
        contact2 = entry_contact2.get().strip()
        email1 = entry_email1.get().strip()
        email2 = entry_email2.get().strip()
        uid = entry_uid.get().strip()

        if not institution_name:
            raise ValueError("Institution Name is required.")
        if not address:
            raise ValueError("Address is required.")
        if not re.match(r'^\d{8}$|^\d{10}$', contact1):
            raise ValueError("Contact 1 is invalid. It must be either 8 or 10 digits.")
        if not re.match(r'^\d{8}$|^\d{10}$', contact2):
            raise ValueError("Contact 2 is invalid. It must be either 8 or 10 digits.")
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email1):
            raise ValueError("Email 1 is invalid.")
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email2):
            raise ValueError("Email 2 is invalid.")
        if len(uid) < 10:
            raise ValueError("UID must be more than 10 characters long.")
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).+$', uid):
            raise ValueError("UID must contain at least one lower case letter, one upper case letter, one digit, and one special character.")
        
        institution_data = ("Institution Name:"+institution_name+"\n"+
            "Address:"+address+"\n"+
            "Contact 1:"+contact1+"\n"+
            "Contact 2:"+contact2+"\n"+
            "Email 1:"+email1+"\n"+
            "Email 2:"+email2+"\n"+
            "UID:"+uid+"\n\n")
            
        messagebox.showinfo("Success", "Institution data submitted successfully!")
        MergeAdmin.save_to_file(institution_data)
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def clear_form():
    entry_institution_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_contact1.delete(0, tk.END)
    entry_contact2.delete(0, tk.END)
    entry_email1.delete(0, tk.END)
    entry_email2.delete(0, tk.END)
    entry_uid.delete(0, tk.END)

def toggle_uid_visibility():
    if entry_uid.cget('show') == '*':
        entry_uid.config(show='')
        view_button.config(text='Hide')
    else:
        entry_uid.config(show='*')
        view_button.config(text='View')

root = tk.Tk()
root.title("Institution Details Form")
root.configure(bg="#e0f7fa")

label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

tk.Label(root, text="Institution Name:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_institution_name = tk.Entry(root, font=entry_font)
entry_institution_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Address:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_address = tk.Entry(root, font=entry_font)
entry_address.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Contact 1:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_contact1 = tk.Entry(root, font=entry_font)
entry_contact1.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Contact 2:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_contact2 = tk.Entry(root, font=entry_font)
entry_contact2.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Email 1:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
entry_email1 = tk.Entry(root, font=entry_font)
entry_email1.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Email 2:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
entry_email2 = tk.Entry(root, font=entry_font)
entry_email2.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="UID:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
entry_uid = tk.Entry(root, show="*", font=entry_font)
entry_uid.grid(row=6, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form, bg="#00796b", fg="white", font=button_font)
submit_button.grid(row=7, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_form, bg="#00796b", fg="white", font=button_font)
clear_button.grid(row=7, column=1, padx=10, pady=10)

view_button = tk.Button(root, text="View", command=toggle_uid_visibility, bg="#00796b", fg="white", font=button_font)
view_button.grid(row=6, column=2, padx=10, pady=10)

root.mainloop()
