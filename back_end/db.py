from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

def get_database_connection():
    uri = os.getenv("MONGO_URI")
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



def sanitize_url(url):
   # Basic example: Replace non-alphanumeric characters with underscores
    # You might want a more comprehensive sanitation process
    return ''.join(e if e.isalnum() else '_' for e in url)


def get_or_create_collection(db, url):
    sanitized_url = sanitize_url(url)
    
    # Check if collection exists
    if sanitized_url not in db.list_collection_names():
        # If not, create it
        db.create_collection(sanitized_url)

    return db[sanitized_url]