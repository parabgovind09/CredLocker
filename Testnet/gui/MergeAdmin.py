import tkinter as tk
import os
import requests
import api.smartcontract.helper.Connection as con
import api.smartcontract.helper.FirebaseHelper as fire
import api.UploadOperation
import api.FileExistenceChecker
import api.DeleteOperation
import api.PinataCredentials
from datetime import datetime
from api.smartcontract.helper.CopyDialog import CopyableDialog as dialog
from tkinter import messagebox
from requests.exceptions import ConnectionError, Timeout, RequestException
from urllib3.exceptions import MaxRetryError

def save_to_file(institution_data,account_address):
    try:
        root = tk.Tk()
        root.withdraw()

        if con.is_internet_available():
            fire_newHash, fire_dateTime, fire_preHash = fire.read_specific_data('AdminRecords/-O-6m7AaYlzXdCQxNZDL')
            if fire_newHash is not None and fire_dateTime is not None and fire_preHash is not None:
                if api.FileExistenceChecker.check_file_existence(fire_newHash):
                    response = requests.get(f'https://gateway.pinata.cloud/ipfs/{fire_newHash}')
                    content = response.text
                    modified_content = "Institution Name: "+institution_data['Institution Name']+" Address: "+institution_data['Address']+" Contact 1: "+institution_data['Contact 1']+" Contact 2: "+institution_data['Contact 2']+" Email 1: "+institution_data['Email 1']+" Email 2: "+institution_data['Email 2']+" Account Address: "+institution_data['Account Address']+" UID: "+institution_data['UID']+" Account Private Key: "+institution_data['Account Private Key']+" Date Time: "+institution_data['Date Time']+content
                    headers = {
                        'Content-Type': 'application/json',
                        'pinata_api_key': api.PinataCredentials.credential['PINATA_API_KEY'],
                        'pinata_secret_api_key': api.PinataCredentials.credential['PINATA_SECRET_API_KEY']
                    }
                    payload = {
                        'pinataOptions': {'cidVersion': 0},
                        'pinataMetadata': {'name': 'AdminRecords.txt'},
                        'pinataContent': modified_content
                    }
                    response = requests.post('https://api.pinata.cloud/pinning/pinJSONToIPFS', headers=headers, json=payload)
                    new_hash = response.json()['IpfsHash']

                    new_data = {
                        "New hash": new_hash,
                        "DateTime": str(datetime.now()),
                        "Previous hash": fire_newHash
                    }
                    fire.update_data('AdminRecords/-O-6m7AaYlzXdCQxNZDL',new_data)
                    if api.DeleteOperation.delete_from_ipfs(fire_newHash):
                        if api.FileExistenceChecker.check_file_existence(fire_newHash):
                            if api.DeleteOperation.delete_from_ipfs(fire_newHash):
                                if api.FileExistenceChecker.check_file_existence(fire_newHash):
                                    return
                                else:
                                    messagebox.showinfo("Success", "Admin Record Recorded")
                            else:
                                old_data = {
                                    "New hash": fire_newHash,
                                    "DateTime": fire_dateTime,
                                    "Previous hash": fire_preHash
                                }
                                messagebox.showerror("Error", "Please check your internet connection and try again.")
                        else:
                            messagebox.showinfo("Success", "Admin Record Recorded")
                    else:
                        old_data = {
                            "New hash": fire_newHash,
                            "DateTime": fire_dateTime,
                            "Previous hash": fire_preHash
                        }
                        fire.update_data('AdminRecords/-O-6A6e9xZ-1LqgMH9Dp',old_data)
                else:
                    messagebox.showerror("Error", "Content Verification Failed with Hosting Database, Please check your internet connection and try again or Contact to Developer")
            else:
                messagebox.showerror("Error", "Please check your internet connection and try again.")
        else:
            messagebox.showerror("Error", "Please check your internet connection and try again.")

        root.mainloop()

    except (ConnectionError, MaxRetryError, Timeout) as e:
        messagebox.showerror("Error", "Please check your internet connection and try again.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Please try again later.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
