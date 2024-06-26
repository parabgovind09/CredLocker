import tkinter as tk
import os
import json
import requests
import api.smartcontract.helper.Connection as con
import api.smartcontract.helper.FirebaseHelper as fire
import api.UploadOperation
import api.FileExistenceChecker
import api.DeleteOperation
import api.PinataCredentials
from datetime import datetime
from tkinter import messagebox
from requests.exceptions import ConnectionError, Timeout, RequestException
from urllib3.exceptions import MaxRetryError

def save_to_file(institution_data,account_address):
    try:
        root = tk.Tk()
        root.withdraw()

        if con.is_internet_available():
            fire_newHash, fire_dateTime, fire_preHash = fire.read_specific_data('AdminRecords/-O-_8pzzSg9kEOg8ib0u')
            if fire_newHash is not None and fire_dateTime is not None and fire_preHash is not None:
                if api.FileExistenceChecker.check_file_existence(fire_newHash):
                    response = requests.get(f'https://gateway.pinata.cloud/ipfs/{fire_newHash}')
                    # Check if the response content is empty
                    if not response.content.strip():
                        content = []  # Set to an empty list if the content is empty
                    else:
                        content = response.json()  # Parse the response as JSON

                        # If the content is a dict, wrap it in a list to maintain consistent structure
                        if isinstance(content, dict):
                            content = [content]
                    modified_content = {
                        "Institution Name": institution_data['Institution Name'],
                        "Address": institution_data['Address'],
                        "Contact 1": institution_data['Contact 1'],
                        "Contact 2": institution_data['Contact 2'],
                        "Email 1": institution_data['Email 1'],
                        "Email 2": institution_data['Email 2'],
                        "Account Address": institution_data['Account Address'],
                        "UID": institution_data['UID'],
                        "Account Private Key": institution_data['Account Private Key'],
                        "Date Time": institution_data['Date Time']
                    }
                    # Append the new record to the existing content
                    content.append(modified_content)
                    headers = {
                        'Content-Type': 'application/json',
                        'pinata_api_key': api.PinataCredentials.credential['PINATA_API_KEY'],
                        'pinata_secret_api_key': api.PinataCredentials.credential['PINATA_SECRET_API_KEY']
                    }
                    payload = {
                        'pinataOptions': {'cidVersion': 0},
                        'pinataMetadata': {'name': 'AdminRecords.json'},
                        'pinataContent': content
                    }
                    response = requests.post('https://api.pinata.cloud/pinning/pinJSONToIPFS', headers=headers, json=payload)
                    new_hash = response.json()['IpfsHash']

                    new_data = {
                        "New hash": new_hash,
                        "DateTime": str(datetime.now()),
                        "Previous hash": fire_newHash
                    }
                    old_data = {
                            "New hash": fire_newHash,
                            "DateTime": fire_dateTime,
                            "Previous hash": fire_preHash
                    }
                    
                    if api.DeleteOperation.delete_from_ipfs(fire_newHash):
                        if fire.update_data('AdminRecords/-O-_8pzzSg9kEOg8ib0u',new_data):
                            messagebox.showinfo("Success", "Admin Record Recorded")
                        else:
                            messagebox.showerror("Error", "Please check your internet connection and try again.")
                    else:
                        messagebox.showerror("Error", "Please check your internet connection and try again.")
                else:
                    messagebox.showerror("Error", "Content Verification Failed with Hosting Database, Please check your internet connection and try again or Contact to Developer")
            else:
                messagebox.showerror("Error", "Failed to Collect Data from Hosting Database, Please check your internet connection and try again.")
        else:
            messagebox.showerror("Error", "Please check your internet connection and try again.")

        root.mainloop()

    except (ConnectionError, MaxRetryError, Timeout) as e:
        messagebox.showerror("Error", "Please check your internet connection and try again.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Please try again later.{e}")
        print(e)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
