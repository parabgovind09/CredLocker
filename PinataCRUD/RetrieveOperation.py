import requests
import DeleteOperation

# Function to retrieve file from IPFS via Pinata
def retrieve_from_ipfs(ipfs_hash):
    
    response = requests.get(f"https://gateway.pinata.cloud/ipfs/{ipfs_hash}")
    if response.status_code == 200:
        file_name = response.url.split('/')[-1]
        return response.content, file_name
    else:
        return None, None

##ipfs_hash = "QmYVAAfnqtEMqBqRggma24kSFY51CZM61JrzYPz9SJVL5m"
##file_content, file_name = retrieve_from_ipfs(ipfs_hash)
##if file_content and file_name:
##    with open(file_name, "wb") as f:
##        f.write(file_content)
##    print("File retrieved from IPFS")
##else:
##    print("File not found on IPFS")