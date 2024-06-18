import requests
import api.FileExistenceChecker

def retrieve_from_ipfs(ipfs_hash):

    if api.FileExistenceChecker.check_file_existence(ipfs_hash):
        response = requests.get(f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}")
        if response.status_code == 200:
            file_name = response.url.split('/')[-1]
            return response.content
    else:
        return None
