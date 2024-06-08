import tkinter as tk
import os
import requests
import api.smartcontract.helper.Connection as con
import api.UploadOperation
import api.FileExistenceChecker
import api.DeleteOperation
from api.smartcontract.helper.CopyDialog import CopyableDialog as dialog
from tkinter import messagebox
from requests.exceptions import ConnectionError, Timeout, RequestException
from urllib3.exceptions import MaxRetryError

def save_to_file(institution_data,account_address,file_name):
    try:
        root = tk.Tk()
        root.withdraw()
        
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        file_path = os.path.join(desktop_path, file_name)
        
        with open(file_path, 'w') as file:
            file.write(str(institution_data))
        
        messagebox.showinfo("Success", f"Data has been written to {file_path}")
        
        if con.is_testnet_connected():
            ipfs_hash = api.UploadOperation.upload_to_ipfs(file_path)
            if ipfs_hash:
                if api.FileExistenceChecker.check_file_existence(ipfs_hash):
                    dialog_obj = dialog(root, "IPFS Hash", ipfs_hash,"File uploaded to IPFS with hash:","Success", "IPFS hash copied to clipboard")
                else:
                    if api.DeleteOperation.delete_from_ipfs(ipfs_hash):
                        messagebox.showerror("Error", "Failed to upload file to IPFS.")
                    else:
                        api.DeleteOperation.delete_from_ipfs(ipfs_hash)
                        messagebox.showerror("Error", "Please check your internet connection and try again.")
            else:
                messagebox.showerror("Error", "Failed to upload file to IPFS.")

        root.mainloop()

    except (ConnectionError, MaxRetryError, Timeout) as e:
        messagebox.showerror("Error", "Please check your internet connection and try again.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Please try again later.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
