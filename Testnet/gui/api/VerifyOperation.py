import api.RetrieveOperation
import api.HashGenerator
import hashlib

def verify_file_contents(ipfs_hash, local_file_path):
    
    # First calculate the hash of the local file
    local_file_hash = api.HashGenerator.calculate_hash(local_file_path)

    # Second retrieve file content from ipfs
    ipfs_file_content = api.RetrieveOperation.retrieve_from_ipfs(ipfs_hash)

    if ipfs_file_content is None:
        print("Error retrieving file from IPFS.")
        return

    # Third calculate the hash of the content fetched from IPFS
    ipfs_hash_calculated = api.HashGenerator.calculate_ipfs_hash(ipfs_file_content)

    # Fourth compare the hashes
    if ipfs_hash_calculated == local_file_hash:
        return True
    else:
        return False
