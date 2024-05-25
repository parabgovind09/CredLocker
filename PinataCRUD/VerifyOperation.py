import RetrieveOperation
import HashGenerator
import hashlib

# Function to verify file contents against IPFS
def verify_file_contents(ipfs_hash, local_file_path):
    
    # First calculate the hash of the local file
    local_file_hash = HashGenerator.calculate_hash(local_file_path)

    # Second retrieve file content and name from IPFS
    ipfs_file_content, ipfs_file_name = RetrieveOperation.retrieve_from_ipfs(ipfs_hash)

    if ipfs_file_content is None and ipfs_file_name is None:
        print("Error retrieving file from IPFS.")
        return

    # Third calculate the hash of the content fetched from IPFS
    ipfs_hash_calculated = HashGenerator.calculate_ipfs_hash(ipfs_file_content)

    # Fourth compare the hashes
    if ipfs_hash_calculated == local_file_hash:
        print("File contents match the contents stored on IPFS.")
    else:
        print("File contents do not match the contents stored on IPFS.")


##ipfs_hash = "QmYVAAfnqtEMqBqRggma24kSFY51CZM61JrzYPz9SJVL5m"
##local_file_path = "C:\\Users\\Minal\\Desktop\\CredLocker\\README.md"
##verify_file_contents(ipfs_hash, local_file_path)
