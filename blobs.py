import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

account_name = os.getenv("YOUR_AZURE_ACCOUNT_NAME")
connect_str1 = os.getenv('AZURE_STORAGE_CONNECTION_STRING1')
connect_str2 =os.getenv('AZURE_STORAGE_CONNECTION_STRING2')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
blob_service_client2 = BlobServiceClient.from_connection_string(connect_str2)

local_path = ".\data"
os.mkdir(local_path)

    # Create a file in the local data directory to upload and download
for i in range(99):
    # Create a unique name for the container
    container_name = str(uuid.uuid4())
    container_name2 = str(uuid.uuid4())
    # Create the container
    container_client = blob_service_client.create_container(container_name)
    container_client2 = blob_service_client2.create_container(container_name2)
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)
    cwd = os.getcwd()
    print(cwd)
    # Write text to the file
    file = open(upload_file_path, 'w')
    file.write("Hello, World!")
    file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client2.get_blob_client(container=container_name2, blob=local_file_name)
    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)
    # Source
    source_container_name = container_name
    source_file_path = local_file_name
    blob_service_client = BlobServiceClient.from_connection_string(connect_str1)
    source_blob = (f"https://{account_name}.blob.core.windows.net/{source_container_name}/{source_file_path}")

    target_container_name = container_name2
    target_file_path = local_file_name
    copied_blob = blob_service_client.get_blob_client(target_container_name, target_file_path)
    copied_blob.start_copy_from_url(source_blob)





