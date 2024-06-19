import tkinter as tk
import json
from tkinter import filedialog, messagebox
from tkinter import font as tkFont
import api.RetrieveOperation
import api.VerifyOperation
import api.smartcontract.helper.AccountContractManager as acc_mgr
from api.smartcontract.helper.CopyDialog import CopyableDialog as dialog

class CredVerify:
    def __init__(self):
        root = tk.Tk()
        root = root
        root.title("CredLocker")
        root.configure(bg='#CF6679')

        self.stored_data = ""
        self.user = ""

        title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        label_font = tkFont.Font(family="Helvetica", size=12)
        button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

        self.label = tk.Label(root, text="Transaction Hash", font=label_font, fg='white', bg='#282c34')
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50, font=label_font, fg='black', bg='white')
        self.entry.pack(pady=10)

        self.retrieve_button = tk.Button(root, text="Retrieve", font=button_font, fg='white', bg='#61afef', command=self.retrieve_transaction)
        self.retrieve_button.pack(pady=10)

        self.verify_button = tk.Button(root, text="Verify", font=button_font, fg='white', bg='#98c379', command=self.verify_transaction)
        self.verify_button.pack(pady=10)

    def retrieve_transaction(self):
        tx_hash = self.entry.get()
        flag, self.user, self.stored_data = acc_mgr.retrieve_data(acc_mgr.contract_address, tx_hash)
        
        if flag and self.user is not None and self.stored_data is not None:
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
