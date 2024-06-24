import tkinter as tk
import json
import random
import smtplib
import time
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import filedialog, messagebox
from tkinter import font as tkFont
import api.smartcontract.helper.FirebaseHelper as fire
import api.smartcontract.helper.Connection as con
import api.RetrieveOperation
import api.ReadFileData
import api.VerifyOperation
import api.smartcontract.helper.AccountContractManager as acc_mgr
import api.smartcontract.helper.OTPManager as otp_mgr
from api.smartcontract.helper.CopyDialog import CopyableDialog as dialog

class CredVerify:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CredLocker")
        self.root.configure(bg='#CF6679')

        self.stored_data = ""
        self.user = ""
        self.tx_hash = ""

        title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        label_font = tkFont.Font(family="Helvetica", size=12)
        button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

        self.label = tk.Label(self.root, text="Transaction Hash", font=label_font, fg='white', bg='#282c34')
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=50, font=label_font, fg='black', bg='white')
        self.entry.pack(pady=10)

        self.retrieve_button = tk.Button(self.root, text="Retrieve", font=button_font, fg='white', bg='#61afef', command=self.retrieve_transaction)
        self.retrieve_button.pack(pady=10)

        self.verify_button = tk.Button(self.root, text="Verify", font=button_font, fg='white', bg='#98c379', command=self.verify_transaction)
        self.verify_button.pack(pady=10)

        self.info_label = tk.Label(self.root, text="Phone No. / Email ID / Aadhaar Number", font=label_font, fg='white', bg='#282c34')
        self.info_label.pack(pady=10)

        self.info_entry = tk.Entry(self.root, width=50, font=label_font, fg='black', bg='white')
        self.info_entry.pack(pady=10)

        self.cert_label = tk.Label(self.root, text="Certificate Type", font=label_font, fg='white', bg='#282c34')
        self.cert_label.pack(pady=10)

        self.cert_entry = tk.Entry(self.root, width=50, font=label_font, fg='black', bg='white')
        self.cert_entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=button_font, fg='white', bg='#d19a66', command=self.submit_info)
        self.submit_button.pack(pady=10)

        self.otp_label = tk.Label(self.root, text="Enter OTP", font=label_font, fg='white', bg='#282c34')
        self.otp_label.pack(pady=10)
        self.otp_label.pack_forget()  # Hide initially

        self.otp_entry = tk.Entry(self.root, width=50, font=label_font, fg='black', bg='white')
        self.otp_entry.pack(pady=10)
        self.otp_entry.pack_forget()  # Hide initially

        self.verify_otp_button = tk.Button(self.root, text="Verify OTP", font=button_font, fg='white', bg='#61afef', command=self.callverify)
        self.verify_otp_button.pack(pady=10)
        self.verify_otp_button.pack_forget()  # Hide initially

    def validate_info(self, info):
        phone_pattern = re.compile(r'^[6-9]\d{9}$')
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        aadhaar_pattern = re.compile(r'^\d{12}$')
        
        if phone_pattern.match(info):
            return 'Phone No.'
        elif email_pattern.match(info):
            return 'Email ID'
        elif aadhaar_pattern.match(info):
            return 'Aadhaar Number'
        else:
            return None

    def callverify(self):
        if otp_mgr.validate_otp(self.otp_entry.get()):

            messagebox.showinfo("Success", "OTP is valid.")
            self.hide_otp_fields()

            
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.tx_hash)
            self.tx_hash = ""
        else:
            messagebox.showerror("Failure", "OTP is invalid or has expired. Try Again")
            self.hide_otp_fields()

    def submit_info(self):
        info = self.info_entry.get()
        cert_type = self.cert_entry.get()
        
        validation_type = self.validate_info(info)
        
        if not cert_type:
            messagebox.showerror("Invalid Entry", "Certificate Type cannot be empty.")
            return
        
        if validation_type:
            if con.is_internet_available():
                fire_newHash, fire_dateTime, fire_preHash = fire.read_specific_data('StudentRecords/-O-_pvGMXImtLxuxmwuM')
                if fire_newHash is not None and fire_dateTime is not None and fire_preHash is not None:
                    if api.FileExistenceChecker.check_file_existence(fire_newHash):
                        byte_data = api.ReadFileData.read_ipfs_content(fire_newHash)
                        json_str = byte_data.decode('utf-8')
                        data = json.loads(json_str)
                        search_term = info
                        search_term1 = cert_type
                        filtered_results = [entry for entry in data if 
                                            (search_term == entry.get('Student Email', '') or
                                             search_term == entry.get('Student Contact', '') or
                                             search_term == entry.get('Aadhar Number', ''))
                                            and (search_term1 == entry.get('Type of Credential', ''))]
                        
                        if filtered_results:
                            for result in filtered_results:
                                messagebox.showinfo("Success", f"{validation_type} is valid and submitted.\nCertificate Type: {cert_type}")
                                otp = otp_mgr.send_otp("vishnuparab0909@gmail.com", "vggc fbaf wngp xagv", info)
                                if otp:
                                    messagebox.showinfo("Success", "OTP sent successfully.")
                                    self.show_otp_fields()
                                    self.tx_hash = result.get('Transaction Hash')
                                else:
                                    messagebox.showerror("Failed", "Failed to send OTP.")
                        else:
                            messagebox.showerror("Error", "No matching data found for the provided credentials.")
                    else:
                        messagebox.showerror("Error", "Content Verification Failed with Hosting Database, Please check your internet connection and try again or Contact to Developer")
                else:
                    messagebox.showerror("Error", "Failed to Collect Data from Hosting Database, Please check your internet connection and try again.")
            else:
                messagebox.showerror("Error", "Please check your internet connection and try again.")
        else:
            messagebox.showerror("Invalid Entry", "Please enter a valid Phone No., Email ID, or Aadhaar Number.")

    def show_otp_fields(self):
        self.otp_label.pack()
        self.otp_entry.pack()
        self.verify_otp_button.pack()

    def hide_otp_fields(self):
        self.otp_label.pack_forget()
        self.otp_entry.pack_forget()
        self.verify_otp_button.pack_forget()

    def retrieve_transaction(self):
        tx_hash = self.entry.get()
        flag, self.user, self.stored_data = acc_mgr.retrieve_data(acc_mgr.contract_address, tx_hash)
        
        if flag and self.user is not None and self.stored_data is not None:
            try:
                loaded_data = json.loads(self.stored_data)
                ipfs = loaded_data['hash']
                name = loaded_data['name']
                
                try:
                    file_content = api.RetrieveOperation.retrieve_from_ipfs(ipfs)
                    if file_content:
                        save_path = filedialog.asksaveasfilename(initialfile=name, title="Save file as")
                        if save_path:
                            with open(save_path, "wb") as f:
                                f.write(file_content)
                            messagebox.showinfo("Success", "File retrieved and saved successfully")
                        else:
                            messagebox.showinfo("Canceled", "Save operation was canceled")
                    else:
                        messagebox.showerror("Failed", "File can't be retrieved from IPFS")
                except Exception as e:
                    messagebox.showerror("Failed", f"Failed to write file content to file: {e}")
            except json.JSONDecodeError as json_err:
                messagebox.showerror("JSON Decode Error", f"Failed to decode JSON data: {json_err}")
        else:
            messagebox.showinfo("Failed", f"No such transaction with hash: {tx_hash}")

        self.stored_data = ""
        self.user = ""

    def verify_transaction(self):
        try:
            tx_hash = self.entry.get()
            flag, self.user, self.stored_data = acc_mgr.retrieve_data(acc_mgr.contract_address, tx_hash)
            
            if flag and self.user is not None and self.stored_data is not None:
                loaded_data = json.loads(self.stored_data)
                ipfs = loaded_data['hash']
                
                local_file_path = filedialog.askopenfilename(title="Select the file to verify")
                
                if local_file_path:
                    try:
                        verification_result = api.VerifyOperation.verify_file_contents(ipfs, local_file_path)
                        if verification_result:
                            messagebox.showinfo("Verification Successful", "The local file matches the IPFS file.")
                        else:
                            messagebox.showerror("Verification Failed", "The local file does not match the IPFS file.")
                    except Exception as e:
                        messagebox.showerror("Verification Failed", f"An error occurred during verification: {e}")
                else:
                    messagebox.showinfo("Canceled", "File selection was canceled.")
            else:
                messagebox.showinfo("Failed", f"No such transaction with hash: {tx_hash}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        self.stored_data = ""
        self.user = ""
