import requests

def read_ipfs_content(ipfs_hash):
    response = requests.get(f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}")
    if response.status_code == 200:
        return response.content
    return None
