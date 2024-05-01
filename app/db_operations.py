# import dependencies
from pymongo import MongoClient
from instance.config import AppConfig
class DbOperations:
    def __init__(self, collection):
        self.client = MongoClient(AppConfig.DB_URI) 
        self.db = self.client[AppConfig.DB_NAME] # database name
        self.collection = self.db[AppConfig.COLLECTION_NAME] # Collection name to be in snake case

    def save_one_to_db(self,data):
        try:
            self.collection.insert_one(data)
            print("Data successfully saved to MongoDB")
        except Exception as e:
            print(f"Error saving data to MongoDB: {e}")

    def query_data_from_db(self, data):
        try:
            self.collection.find(data)
            print('Data successfully retrieved')
        except Exception as e:
            print(f'Data not found')

    

