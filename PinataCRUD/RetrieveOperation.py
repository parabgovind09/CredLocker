import requests
import FileExistenceChecker

# Function to retrieve file from IPFS via Pinata
def retrieve_from_ipfs(ipfs_hash):

    if FileExistenceChecker.check_file_existence(ipfs_hash):
        response = requests.get(f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}")
        if response.status_code == 200:
            file_name = response.url.split('/')[-1]
            print("File retrieved from IPFS")
            return response.content, file_name
    else:
        print("File can't be retrieved from IPFS")
        return None, None

##ipfs_hash = "QmRSDGXdZx7PZbLAWMT39xH9HWAnXHHMvHUhLC7VmMoA9h"
##file_content, file_name = retrieve_from_ipfs(ipfs_hash)
##if file_content and file_name:
##    with open(file_name, "wb") as f:
##        f.write(file_content)
##    print("File retrieved from IPFS")
##else:
##    print("File can't be retrieved from IPFS")
