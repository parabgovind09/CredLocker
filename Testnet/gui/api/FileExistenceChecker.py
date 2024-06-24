import requests
import api.PinataCredentials

def check_file_existence(file_hash):
    
    response = requests.get("https://api.pinata.cloud/data/pinList?status=pinned", headers=api.PinataCredentials.credential)
    if response.status_code == 200:
        data = response.json()
        # Iterate through pinned items to check if file exists
        for item in data['rows']:
            if item['ipfs_pin_hash'] == file_hash:
                return True
        return False
    else:
        return False
