import requests
import api.PinataCredentials

# Function to check if a file exists on IPFS
def check_file_existence(file_hash):
    
    response = requests.get("https://api.pinata.cloud/data/pinList?status=pinned", headers=api.PinataCredentials.credential)
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        # Iterate through pinned items to check if file exists
        for item in data['rows']:
            if item['ipfs_pin_hash'] == file_hash:
                return True
        return False
    else:
        return False
