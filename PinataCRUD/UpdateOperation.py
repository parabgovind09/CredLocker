import requests
import UploadOperation
import DeleteOperation

# Function to update file on IPFS via Pinata
def update_on_ipfs(old_ipfs_hash, new_file_path):
    # First upload the new version of the file
    new_ipfs_hash = UploadOperation.upload_to_ipfs(new_file_path)
    if new_ipfs_hash is None:
        print("Failed to upload new file to IPFS")
        return False

    # Delete the old version of the file
    DeleteOperation.delete_from_ipfs(old_ipfs_hash)

    return new_ipfs_hash


##old_ipfs_hash = "QmRSDGXdZx7PZbLAWMT39xH9HWAnXHHMvHUhLC7VmMoA9h"
##new_file_path = "C:\\Users\\Minal\\Desktop\\CredLocker\\README.md"
##
##updated_ipfs_hash = update_on_ipfs(old_ipfs_hash, new_file_path)
##if updated_ipfs_hash:
##    print("File updated on IPFS. New IPFS hash:", updated_ipfs_hash)
##else:
##    print("Failed to update file on IPFS")
