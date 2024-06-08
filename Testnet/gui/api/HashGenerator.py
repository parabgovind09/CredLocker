import hashlib

# Function to calculate the hash of a file
def calculate_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


# Function to calculate the hash of a ipfs file content
def calculate_ipfs_hash(ipfs_file_content):
    hasher = hashlib.sha256()
    chunk_size = 4096
    while True:
        chunk = ipfs_file_content[:chunk_size]
        if not chunk:
            break
        hasher.update(chunk)
        ipfs_file_content = ipfs_file_content[chunk_size:]
    return hasher.hexdigest()
