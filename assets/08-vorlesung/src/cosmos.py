import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import datetime

import cosmos_config as cfg

# ----------------------------------------------------------------------------------------------------------
# Prerequistes - 
# 
# 1. An Azure Cosmos account - 
#    https:#azure.microsoft.com/en-us/documentation/articles/documentdb-create-account/
#
# 2. Microsoft Azure Cosmos PyPi package - 
#    https://pypi.python.org/pypi/azure-cosmos/
# ----------------------------------------------------------------------------------------------------------
# Sample - demonstrates the basic CRUD operations on a Database resource for Azure Cosmos
#
# 1. Query for Database (QueryDatabases)
#
# 2. Create Database (CreateDatabase)
#
# 3. Get a Database by its Id property (ReadDatabase)
#
# 4. List all Database resources on an account (ReadDatabases)
#
# 5. Delete a Database given its Id property (DeleteDatabase)
# ----------------------------------------------------------------------------------------------------------

HOST = cfg.settings['host']
MASTER_KEY = cfg.settings['master_key']
DATABASE_ID = cfg.settings['database_id']
COLLECTION_ID = cfg.settings['collection_id']

database_link = 'dbs/' + DATABASE_ID
collection_link = database_link + '/colls/' + COLLECTION_ID

class IDisposable(cosmos_client.CosmosClient):
    """ A context manager to automatically close an object with a close method
    in a with statement. """

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        # extra cleanup in here
        self.obj = None

def create_cosmos_client():
    return cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY} )

class DocumentManagement:

    @staticmethod
    def CreateDocument(client, data):
        print('Creating Cosmos Documents ' + data)
        client.CreateItem(collection_link, data)
    
    @staticmethod
    def CreateDocuments(client):
        print('Creating Documents')

        # Create a device object. This object has nested properties and various types including numbers, DateTimes and strings.
        # This can be saved as JSON as is without converting into rows/columns.
        device1 = DocumentManagement.GetDevice1("Device1")
        client.CreateItem(collection_link, device1)

        # You can insert device2 objects without any 
        # changes to the database tier.
        device2 = DocumentManagement.GetDevice2("Device2")
        client.CreateItem(collection_link, device2)

            

    @staticmethod
    def QueryDocument(client, doc_id, count = 2):
        # Query these items in SQL
        query = {'query': "SELECT * FROM c WHERE c.DeviceId=@id",
                'parameters':[
                    {'name': '@id', 'value' : 'Device1'}
                    ]
                }

        options = {}
        options['enableCrossPartitionQuery'] = True
        options['maxItemCount'] = count

        collectionLink = '/dbs/pysamples/colls/devices/'
        result_iterable = client.QueryItems(collectionLink, query, options)
        for item in iter(result_iterable):
            print(item)  

    @staticmethod
    def ReadDocument(client, doc_id):
        print('Read Document by Id\n')

        # Note that Reads require a partition key to be spcified. This can be skipped if your collection is not
        # partitioned i.e. does not have a partition key definition during creation.
        doc_link = collection_link + '/devices/DeviceId=' + doc_id
        response = client.ReadItem(doc_link)

        print('Document read by Id {0}'.format(doc_id))
        print('DeviceId   : {0}'.format(response.get('DviceId')))
        print('Device data: {0}'.format(response.get('Devicedata')))

    @staticmethod
    def ReadDocuments(client):
        print('\nReading all documents in a collection\n')

        # NOTE: Use MaxItemCount on Options to control how many documents come back per trip to the server
        #       Important to handle throttles whenever you are doing operations such as this that might
        #       result in a 429 (throttled request)
        documentlist = list(client.ReadItems(collection_link, {'maxItemCount':10}))
        
        print('Found {0} devices'.format(documentlist.__len__()))
        
        for doc in documentlist:
            print('Device Id: {0}'.format(doc.get('id')))

    @staticmethod
    def GetDevice1(document_id):
        d1 = {  'DeviceId' : document_id,
                'Devicedata' : 'some device data',
                'MAC'        : 'PO18009186470',
                'date'       : datetime.date(2005,1,10).strftime('%c'),
                'CO2'        : 419.4589,
                'temp'       : 12.5838,
                'Noise'      : 985.018,
                'ttl'        : 60 * 60 * 24 * 30,
                'Version'    : 1
                }

        return d1

    @staticmethod
    def GetDevice2(document_id):
        # notice new fields have been added to the sales order
        d2 = {'Deviceid' : document_id,
                'Devicedata' : 'Account2',
                'MAC' : 'PO15428132599',
                'start_date' : datetime.date(2005,7,11).strftime('%c'),
                'end_date'   : datetime.date(2005,7,21).strftime('%c'),
                'CO2'   : 586.1203,
                'temp'  : 18.1626,
                'Noise' : 1982.872,
                'Light' : 13.3,
                'Pred'  : [
                    {'People'  : 3,
                     'model'   : 'People',      
                     'version' : 'v1'          
                    }
                    ],
                'ttl' : 60 * 60 * 24 * 30,
                'Version'   : 2
                }

        return d2

def run_sample():
    with IDisposable(cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY} )) as client:
        try:
            # setup database for this sample
            try:
                client.CreateDatabase({"id": DATABASE_ID})

            except errors.HTTPFailure as e:
                if e.status_code == 409:
                    pass
                else:
                    raise

            # setup collection for this sample
            try:
                client.CreateContainer(database_link, {"id": COLLECTION_ID})
                print('Collection with id \'{0}\' created'.format(COLLECTION_ID))

            except errors.HTTPFailure as e:
                if e.status_code == 409:
                    print('Collection with id \'{0}\' was found'.format(COLLECTION_ID))
                else:
                    raise

            # DocumentManagement.CreateDocuments(client)
            DocumentManagement.QueryDocument(client,'Device1, 2')
            # DocumentManagement.ReadDocument(client,'Device1')
            #DocumentManagement.ReadDocuments(client)

        except errors.HTTPFailure as e:
            print('\nrun_sample has caught an error. {0}'.format(e))
        
        finally:
            print("\nrun_sample done")

if __name__ == '__main__':
    try:
        run_sample()

    except Exception as e:
        print("Top level Error: args:{0}, message:N/A".format(e.args))