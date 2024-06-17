import json
import requests
import api.smartcontract.helper.Connection as con
import api.smartcontract.helper.FirebaseHelper as fire
import api.PinataCredentials
import api.UploadOperation
import api.FileExistenceChecker
import api.DeleteOperation
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from requests.exceptions import ConnectionError, Timeout, RequestException
from urllib3.exceptions import MaxRetryError

def record_transaction_to_ipfs(student_data):
    try:
        if con.is_internet_available():
            fire_newHash, fire_dateTime, fire_preHash = fire.read_specific_data('StudentRecords/-O-_pvGMXImtLxuxmwuM')
            if fire_newHash is not None and fire_dateTime is not None and fire_preHash is not None:
                if api.FileExistenceChecker.check_file_existence(fire_newHash):
                    response = requests.get(f'https://gateway.pinata.cloud/ipfs/{fire_newHash}')
                    if not response.content.strip():
                        content = []
                    else:
                        content = response.json()
                        if isinstance(content, dict):
                            content = [content]
                    content.append(student_data)
                    headers = {
                        'Content-Type': 'application/json',
                        'pinata_api_key': api.PinataCredentials.credential['PINATA_API_KEY'],
                        'pinata_secret_api_key': api.PinataCredentials.credential['PINATA_SECRET_API_KEY']
                    }
                    payload = {
                        'pinataOptions': {'cidVersion': 0},
                        'pinataMetadata': {'name': 'StudentRecords.json'},
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
                        if fire.update_data('StudentRecords/-O-_pvGMXImtLxuxmwuM',new_data):
                            messagebox.showinfo("Success", "Student Record Recorded")
                        else:
                            messagebox.showerror("Error", "Please check your internet connection and try again.")                           
                    else:
                        messagebox.showerror("Error", "Please check your internet connection and try again.")
                else:
                    messagebox.showerror("Error", "Content Verification Failed with Hosting Database, Please check your internet connection and try again or Contact to Developer")
            else:
                messagebox.showerror("Error", "Failed to Collect Data from Hosting Database, Please check your internet connection and try again.")
        else:
            messagebox.showerror("Error", "Please check your internet connection and try again later.")

        student_data = {}

    except (ConnectionError, MaxRetryError, Timeout) as e:
        messagebox.showerror("Error", "Please check your internet connection and try again.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Please try again later.{e}")
        print(e)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
