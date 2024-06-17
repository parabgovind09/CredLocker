import requests
import api.PinataCredentials

# Function to upload file to IPFS via Pinata
def upload_to_ipfs(file_path):
    files = {'file': open(file_path, 'rb')}
    response = requests.post('https://api.pinata.cloud/pinning/pinFileToIPFS', files=files, headers=api.PinataCredentials.credential)
    if response.status_code == 200:
        return response.json()['IpfsHash']
    else:
        return None
