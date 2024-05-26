import requests
from PinataCredentials import credential
import requests

# Function to check if a file exists on IPFS
def check_file_existence(file_hash):
    
    response = requests.get("https://api.pinata.cloud/data/pinList?status=pinned", headers=credential)
    
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        # Iterate through pinned items to check if file exists
        for item in data['rows']:
            if item['ipfs_pin_hash'] == file_hash:
                print("File exist on IPFS")
                return True
        print("File doesn't exist on IPFS")
        return False
    else:
        print(f"Failed to retrieve pinned items. Status Code: {response.status_code}")
        return False

##check_file_existence("QmRSDGXdZx7PZbLAWMT39xH9HWAnXHHMvHUhLC7VmMoA9h")
