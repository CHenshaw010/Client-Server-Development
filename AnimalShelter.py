from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # USER = 'aacuser'
        # PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31810
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print('Connection Established!')

    # Create method to implement the C in CRUD.
    def create(self, data):
        try:
            if data is not None:
                # Insert user passed data into the collection
                insert = self.database.animals.insert_one(data)  # data should be dictionary
                if insert is not None:
                    # return true indicating procedure finished properly
                    return True
            else:
                raise Exception("Nothing to save, because data parameter is empty")
        except:
            # return false indicating procedure failed
            return False

    # Read method to implement the R in CRUD.
    def read(self, readData):
        if readData is not None:
            # Find all matching data
            result = list(self.database.animals.find(readData))
            if result is not None:
                # return list of matching data
                return result
            else:
                # return an empty list
                return []
        else:
            raise Exception("Nothing to search, because data parameter is empty")

    # Update method to implement the U in CRUD.
    def update(self, dataToUpdate, newData):
        if dataToUpdate or newData is not None:
            # Find and update all matching data
            updated = self.database.animals.update_many(dataToUpdate, {"$set": newData})
            # return cursor object containing updated count
            return updated
        else:
            raise Exception("Nothing to update, because data parameter is empty")

    # Delete method to implement the D in CRUD.
    def delete(self, dataToDelete):
        if dataToDelete is not None:
            # Find and delete all matching data
            deleted = self.database.animals.delete_many(dataToDelete)
            # return cursor object containing deleted count
            return deleted
        else:
            raise Exception("Nothing to delete, because data parameter is empty")