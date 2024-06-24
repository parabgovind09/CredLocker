import requests
import api.FileExistenceChecker

def read_ipfs_content(ipfs_hash):
    if api.FileExistenceChecker.check_file_existence(ipfs_hash):
        response = requests.get(f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}")
        if response.status_code == 200:
            return response.content
        else:
            return None
    else:
        return None
