import os
import io
import uuid
import json
from azure.storage.blob import BlockBlobService, PublicAccess

# ----------------------------------------------------------------------------------------------------------
# Prerequistes - 
# 
# 1. An Azure Storage account - 
#
# 2. Microsoft Azure Blob Storage PyPi package - pip install azure-storage-blob
#    
# ----------------------------------------------------------------------------------------------------------
# Sample - demonstrates the basic create and read operations on a Azure Blob storage
#
# 1. Create Container (create_container)
#
# 2. Write file
#
# 3. Write data
#
# 4. List all resources from container (list_blobs)
#
# ----------------------------------------------------------------------------------------------------------

class Blob():
    """ A blob wrapper class.

    """

    def __init__(self, container_name='devices', local_path = '.\Data'):

        """  Creates a new instance of the blob wrapper class
        """

        # Create the BlockBlockService that is used to call the Blob service for the storage account.
        self.blob_service = BlockBlobService(account_name = 'iotinfstore', account_key = 'VxbwD/Cjvfi+ZObPIkqZ7AT8NKG3AqF6m0jYEUiwU12xtpiotyxIRNRyKu208P1+W+DdYKZd0SzFii2SrcsgWQ==') 

        # local data path
        self.local_path = os.path.expanduser(local_path)    

        # Create a container called 'quickstartblobs'.
        self.container_name = container_name

        self.blob_service.create_container(container_name) 
        # Set the permission so the blobs are public.
        self.blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)



    def create_sample_content(self):
    
        """ Creates a simple dummy document
        """    

        # Create a file in Documents to test the upload and download.
        local_file_name = "Data_" + str(uuid.uuid4()) + ".txt"
        full_path_to_file = os.path.join(self.local_path, local_file_name)
        # Write text to the file.
        file = open(full_path_to_file, 'w')
        file.write("Hello, World!")
        file.close()
        print("Temp file = " + full_path_to_file)


    def upload_file_to_blob(self, local_file_name):

        """ Uploads a fila as blob to böob storage
        """

        print("\nUploading to Blob storage as blob " + local_file_name)
        full_path_to_file = os.path.join(self.local_path, local_file_name)
        print(full_path_to_file)
        # Upload the created file, use local_file_name for the blob name.
        self.blob_service.create_blob_from_path(self.container_name, local_file_name, full_path_to_file)

    def write_data_to_blob(self,data):
        
        """ Writes data to blob storage with uuid as filename
        """

        self.blob_service.create_blob_from_text(self.container_name, str(uuid.uuid4()), data)

    def list_blob_content(self):

        """ Receives the list of all files from blob storage
        """

        # List the blobs in the container.
        print("\nList blobs in the container")
        generator = self.blob_service.list_blobs(self.container_name)
        for blob in generator:
            print("\t Blob name: " + blob.name)


# Main
if __name__ == '__main__':
    try:
        blob = Blob('devices', '.\Data')
        blob.write_data_to_blob('titanic.csv')
        blob.write_data_to_blob(json.dumps({'DeviceId': str(uuid.uuid1()),'Temp': 12.1}))
        blob.list_blob_content()

    except Exception as e:
        print("Top level Error: args:{0}, message:N/A".format(e.args))