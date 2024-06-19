import tkinter as tk
import re
import MergeAdmin
import api.smartcontract.helper.Balance as bal
import api.smartcontract.helper.Connection as con
from tkinter import messagebox
from datetime import datetime
from eth_account import Account

class AddAdminGUI:
    def __init__(self):
        root = tk.Tk()
        root = root
        root.title("CredLocker")
        root.configure(bg='#228b22')

        self.label_font = ("Helvetica", 15, "bold")
        self.entry_font = ("Helvetica", 15)
        self.button_font = ("Helvetica", 12, "bold")

        self.create_widgets(root)

    def create_widgets(self,root):
        tk.Label(root, text="Institution Name:", bg="#228b22", fg="#000000", font=self.label_font).grid(row=0, column=0, padx=15, pady=5, sticky=tk.W)
        self.entry_institution_name = tk.Entry(root, font=self.entry_font)
        self.entry_institution_name.grid(row=0, column=1, padx=15, pady=5)

        tk.Label(root, text="Address:", bg="#228b22", fg="#000000", font=self.label_font).grid(row=1, column=0, padx=15, pady=5, sticky=tk.W)
        self.entry_address = tk.Entry(root, font=self.entry_font)
        self.entry_address.grid(row=1, column=1, padx=15, pady=5)

        tk.Label(root, text="Contact 1:", bg="#228b22", fg="#000000", font=self.label_font).grid(row=2, column=0, padx=15, pady=5, sticky=tk.W)
        self.entry_contact1 = tk.Entry(root, font=self.entry_font)
        self.entry_contact1.grid(row=2, column=1, padx=15, pady=5)

        tk.Label(root, text="Contact 2:", bg="#228b22", fg="#000000", font=self.label_font).grid(row=3, column=0, padx=15, pady=5, sticky=tk.W)
        self.entry_contact2 = tk.Entry(root, font=self.entry_font)
        self.entry_contact2.grid(row=3, column=1, padx=15, pady=5)

        tk.Label(root, text="Email 1:", bg="#228b22", fg="#000000", font=self.label_font).grid(row=4, column=0, padx=15, pady=5, sticky=tk.W)
        self.entry_email1 = tk.Entry(root, font=self.entry_font)
        self.entry_email1.grid(row=4, column=1, padx=15, pady=5)

        tk.Label(root, text="Email 2:", bg="#228b22", fg="#000000", font=self.label_font).grid(row=5, column=0, padx=15, pady=5, sticky=tk.W)
        self.entry_email2 = tk.Entry(root, font=self.entry_font)
        self.entry_email2.grid(row=5, column=1, padx=15, pady=5)

        tk.Label(root, text="Account Address:", bg="#228b22", fg="#000000", font=self.label_font).grid(row=6, column=0, padx=15, pady=5, sticky=tk.W)
        self.entry_account_address = tk.Entry(root, font=self.entry_font)
        self.entry_account_address.grid(row=6, column=1, padx=15, pady=5)

        tk.Label(root, text="UID:", bg="#228b22", fg="#000000", font=self.label_font).grid(row=7, column=0, padx=15, pady=5, sticky=tk.W)
        self.entry_uid = tk.Entry(root, show="*", font=self.entry_font)
        self.entry_uid.grid(row=7, column=1, padx=15, pady=5)

        tk.Label(root, text="Account Private Key:", bg="#228b22", fg="#000000", font=self.label_font).grid(row=8, column=0, padx=15, pady=5, sticky=tk.W)
        self.entry_account_private_key = tk.Entry(root, show="*", font=self.entry_font)
        self.entry_account_private_key.grid(row=8, column=1, padx=15, pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_form, bg="#228b22", fg="#f2f2f2", font=self.button_font)
        self.submit_button.grid(row=9, column=0, padx=15, pady=15)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_form, bg="#228b22", fg="#f2f2f2", font=self.button_font)
        self.clear_button.grid(row=9, column=1, padx=15, pady=15)

        self.view_button = tk.Button(root, text="View", command=self.toggle_uid_visibility, bg="#228b22", fg="#f2f2f2", font=self.button_font)
        self.view_button.grid(row=7, column=2, padx=15, pady=15)

    def submit_form(self):
        try:
            institution_name = self.entry_institution_name.get().strip()
            address = self.entry_address.get().strip()
            contact1 = self.entry_contact1.get().strip()
            contact2 = self.entry_contact2.get().strip()
            email1 = self.entry_email1.get().strip()
            email2 = self.entry_email2.get().strip()
            account_address = self.entry_account_address.get().strip()
            uid = self.entry_uid.get().strip()
            account_private_key = self.entry_account_private_key.get().strip()

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
            if not account_private_key:
                raise ValueError("Account Private Key is required.")

            institution_data = {
                "Institution Name": institution_name,
                "Address": address,
                "Contact 1": contact1,
                "Contact 2": contact2,
                "Email 1": email1,
                "Email 2": email2,
                "Account Address": account_address,
                "UID": uid,
                "Account Private Key": account_private_key,
                "Date Time": str(datetime.now())
            }

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
                MergeAdmin.save_to_file(institution_data, account_address)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def clear_form(self):
        self.entry_institution_name.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_contact1.delete(0, tk.END)
        self.entry_contact2.delete(0, tk.END)
        self.entry_email1.delete(0, tk.END)
        self.entry_email2.delete(0, tk.END)
        self.entry_account_address.delete(0, tk.END)
        self.entry_uid.delete(0, tk.END)
        self.entry_account_private_key.delete(0, tk.END)

    def toggle_uid_visibility(self):
        if self.entry_uid.cget('show') == '*':
            self.entry_uid.config(show='')
            self.view_button.config(text='Hide')
        else:
            self.entry_uid.config(show='*')
            self.view_button.config(text='View')
