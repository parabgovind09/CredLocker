import tkinter as tk
import re
import MergeAdmin
import api.smartcontract.helper.Balance as bal
import api.smartcontract.helper.Connection as con
from tkinter import messagebox
from datetime import datetime
from eth_account import Account

def submit_form():
    try:
        institution_name = entry_institution_name.get().strip()
        address = entry_address.get().strip()
        contact1 = entry_contact1.get().strip()
        contact2 = entry_contact2.get().strip()
        email1 = entry_email1.get().strip()
        email2 = entry_email2.get().strip()
        account_address = entry_account_address.get().strip()
        uid = entry_uid.get().strip()
        account_private_key = entry_account_private_key.get().strip()  # New field
        file_name = entry_file_name.get().strip()

        if not institution_name:
            raise ValueError("Institution Name is required.")
        if not address:
            raise ValueError("Address is required.")
        if not re.match(r'^\d{8}$|^\d{10}$', contact1):
            raise ValueError("Contact 1 is invalid. It must be either 8 or 10 digits.")
        if not re.match(r'^\d{8}$|^\d{10}$', contact2):
            raise ValueError("Contact 2 is invalid. It must be either 8 or 10 digits.")
        if contact1 == contact2:
            raise ValueError("Contact 1 and Contact 2 cannot be the same.")
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email1):
            raise ValueError("Email 1 is invalid.")
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email2):
            raise ValueError("Email 2 is invalid.")
        if email1 == email2:
            raise ValueError("Email 1 and Email 2 cannot be the same.")
        if not account_address:
            raise ValueError("Account Address is required.")
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).+$', uid):
            raise ValueError("UID must contain at least one lower case letter, one upper case letter, one digit, and one special character.")
        if len(uid) < 10:
            raise ValueError("UID must be more than 10 characters long.")
        if not file_name:
            raise ValueError("File Name is required.")
        if not account_private_key:
            raise ValueError("Account Private Key is required.")

        institution_data = (
            f"Institution Name: {institution_name}\n"
            f"Address: {address}\n"
            f"Contact 1: {contact1}\n"
            f"Contact 2: {contact2}\n"
            f"Email 1: {email1}\n"
            f"Email 2: {email2}\n"
            f"Account Address: {account_address}\n"
            f"UID: {uid}\n"
            f"Account Private Key: {account_private_key}\n"
            f"File Name: {file_name}\n"
            "Date Time: " + str(datetime.now()) + "\n\n"
        )
        
        if not con.w3.is_address(account_address):
            messagebox.showerror("Error", "Invalid Account Address!!")
            return None

        account = Account.from_key(account_private_key)
        address = account.address
    
        if not address.lower() == account_address.lower():
            messagebox.showerror("Error", "Private key does not belongs to provided account address")
            return None
        
        thres = bal.get_threshold_ether()
        acc_bal = bal.get_balance(account_address)
        
        if thres >= acc_bal:
            messagebox.showinfo("Failed", "Your Account balance is " + str(acc_bal) + " which is not more than minimum required balance which is " + str(thres))
        else:
            messagebox.showinfo("Success", "Your Account balance is " + str(acc_bal) + " which is greater than minimum required balance which is " + str(thres))
            messagebox.showinfo("Success", "Institution data submitted successfully!")
            MergeAdmin.save_to_file(institution_data, account_address, file_name)

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
    entry_account_address.delete(0, tk.END)
    entry_uid.delete(0, tk.END)
    entry_account_private_key.delete(0, tk.END)  # Clear the new field
    entry_file_name.delete(0, tk.END)

def toggle_uid_visibility():
    if entry_uid.cget('show') == '*':
        entry_uid.config(show='')
        view_button.config(text='Hide')
    else:
        entry_uid.config(show='*')
        view_button.config(text='View')

def record_transaction():
    messagebox.showinfo("Transaction", "Record Transaction button clicked!")

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

tk.Label(root, text="Account Address:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
entry_account_address = tk.Entry(root, font=entry_font)
entry_account_address.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="UID:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
entry_uid = tk.Entry(root, show="*", font=entry_font)
entry_uid.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="File Name:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
entry_file_name = tk.Entry(root, font=entry_font)
entry_file_name.grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="Account Private Key:", bg="#e0f7fa", fg="#00796b", font=label_font).grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)
entry_account_private_key = tk.Entry(root, show="*", font=entry_font)
entry_account_private_key.grid(row=9, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form, bg="#00796b", fg="white", font=button_font)
submit_button.grid(row=10, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_form, bg="#00796b", fg="white", font=button_font)
clear_button.grid(row=10, column=1, padx=10, pady=10)

view_button = tk.Button(root, text="View", command=toggle_uid_visibility, bg="#00796b", fg="white", font=button_font)
view_button.grid(row=7, column=2, padx=10, pady=10)

record_button = tk.Button(root, text="Record Transaction", command=record_transaction, bg="#00796b", fg="white", font=button_font)
record_button.grid(row=10, column=2, padx=10, pady=10)

root.mainloop()
