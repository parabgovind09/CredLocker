import requests
from PinataCredentials import credential
import FileExistenceChecker

# Function to delete file on IPFS via Pinata
def delete_from_ipfs(ipfs_hash):

    if FileExistenceChecker.check_file_existence(ipfs_hash):
        
        response = requests.delete(f"https://api.pinata.cloud/pinning/unpin/{ipfs_hash}", headers=credential)
        if response.status_code == 200:
            print("File deleted from IPFS")
            return True
    else:
        print("Error file can't be deleted from IPFS")
        return False

##deleted = delete_from_ipfs("QmRSDGXdZx7PZbLAWMT39xH9HWAnXHHMvHUhLC7VmMoA9h")
##if deleted:
##    print("File deleted from IPFS")
##else:
##    print("File not found on IPFS")
