from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi




def get_database_connection():
    uri = "mongodb+srv://hassansyed123:6Fpi9TNnTGxo76cF@cluster0.edhu2ca.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.get_database("YTLiveChat")
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!\n")
    except Exception as e:
        print(e)
    
    return db

def insert_document(collection, document):
    collection.insert_one(document)