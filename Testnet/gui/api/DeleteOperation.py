import requests
import api.PinataCredentials
import api.FileExistenceChecker

def delete_from_ipfs(ipfs_hash):

    if api.FileExistenceChecker.check_file_existence(ipfs_hash):
        
        response = requests.delete(f"https://api.pinata.cloud/pinning/unpin/{ipfs_hash}", headers=api.PinataCredentials.credential)
        if response.status_code == 200:
            return True
    else:
        return False

