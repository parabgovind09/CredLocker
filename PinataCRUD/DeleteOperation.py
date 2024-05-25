import requests
from PinataCredentials import credential

# Function to delete file on IPFS via Pinata
def delete_from_ipfs(ipfs_hash):

    response = requests.delete(f"https://api.pinata.cloud/pinning/unpin/{ipfs_hash}", headers=credential)

    if response.status_code == 200:
        return True
    else:
        print("Error:", response.text)
        return False



##ipfs_hash = "QmYVAAfnqtEMqBqRggma24kSFY51CZM61JrzYPz9SJVL5m"
##deleted = delete_from_ipfs(ipfs_hash)
##if deleted:
##    print("File deleted from IPFS")
##else:
##    print("File not found on IPFS")
