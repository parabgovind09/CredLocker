import requests
from PinataCredentials import credential

# Function to upload file to IPFS via Pinata
def upload_to_ipfs(file_path):

    files = {'file': open(file_path, 'rb')}
    response = requests.post('https://api.pinata.cloud/pinning/pinFileToIPFS', files=files, headers=credential)
    if response.status_code == 200:
        return response.json()['IpfsHash']
    else:
        return None

##ipfs_hash = upload_to_ipfs("C:\\Users\\Minal\\Desktop\\CredLocker\\README.md")
##print("File uploaded to IPFS with hash:", ipfs_hash)

#QmYVAAfnqtEMqBqRggma24kSFY51CZM61JrzYPz9SJVL5m
