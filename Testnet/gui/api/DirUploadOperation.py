from os import walk, path, sep
from requests import Session, Request
import json

def pinata_upload(directory):
    files = []
    ipfs_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        'pinata_api_key': "d5deb29ab66ea973f31a",
        'pinata_secret_api_key': "b7bd1067e790a58ca4798295738d053fe63b27ad7056b7df9dcfe3d513a2d733"
    }

    # Normalize directory path
    normalized_directory = path.normpath(directory)
    directory_name = path.basename(normalized_directory)
    metadata = json.dumps({"name": directory_name})

    # Add metadata to files
    files.append(('pinataMetadata', (None, metadata)))

    # Store file objects to keep them open
    file_objects = []

    # Traverse the directory and collect files
    for root, dirs, files_ in walk(normalized_directory):
        for f in files_:
            complete_path = path.join(root, f)
            normalized_path = path.normpath(complete_path)
            # Convert to relative path with forward slashes
            relative_path = sep.join(normalized_path.split(sep)[-2:]).replace(sep, '/')
            file_obj = open(complete_path, 'rb')
            file_objects.append(file_obj)
            files.append(('file', (relative_path, file_obj)))

    # Prepare and send the request
    try:
        request = Request(
            'POST',
            ipfs_url,
            headers=headers,
            files=files
        ).prepare()
        response = Session().send(request)

        print(response.request.url)
        print(response.request.headers)
        print(response.request.body)
        print(response.json())

        return response.json().get('IpfsHash')

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Close all file objects
        for file_obj in file_objects:
            file_obj.close()

if __name__ == '__main__':
    directory_path = r'C:\Users\Minal\Desktop\Newfolder'
    ipfs_hash = pinata_upload(directory_path)
    print(f"Uploaded Directory IPFS Hash: {ipfs_hash}")
