import tkinter as tk
import json
from tkinter import filedialog, messagebox
from tkinter import font as tkFont
import api.RetrieveOperation
import api.VerifyOperation
import api.smartcontract.helper.AccountContractManager as acc_mgr
from api.smartcontract.helper.CopyDialog import CopyableDialog as dialog

stored_data = ""
user = ""

def retrieve_transaction():
    tx_hash = entry.get()
    global stored_data
    global user
    flag, user, stored_data = acc_mgr.retrieve_data(acc_mgr.contract_address, tx_hash)
    
    if flag and user is not None and stored_data is not None:
        loaded_data = json.loads(stored_data)
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

    stored_data = ""
    user = ""

def verify_transaction():
    global stored_data
    global user
    try:
        tx_hash = entry.get()
        flag, user, stored_data = acc_mgr.retrieve_data(acc_mgr.contract_address, tx_hash)
        
        if flag and user is not None and stored_data is not None:
            loaded_data = json.loads(stored_data)
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

    stored_data = ""
    user = ""

root = tk.Tk()
root.title("CredLocker")
root.configure(bg='#CF6679')

title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
label_font = tkFont.Font(family="Helvetica", size=12)
button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

label = tk.Label(root, text="Transaction Hash", font=label_font, fg='white', bg='#282c34')
label.pack(pady=10)

entry = tk.Entry(root, width=50, font=label_font, fg='black', bg='white')
entry.pack(pady=10)

retrieve_button = tk.Button(root, text="Retrieve", font=button_font, fg='white', bg='#61afef', command=retrieve_transaction)
retrieve_button.pack(pady=10)

verify_button = tk.Button(root, text="Verify", font=button_font, fg='white', bg='#98c379', command=verify_transaction)
verify_button.pack(pady=10)

root.mainloop()
