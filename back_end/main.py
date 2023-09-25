

from app import capture_chat_data
from db import get_database_connection, insert_document
from analytics import get_hype_moments, get_moments
def main():

    # Prompt user for YouTube live stream URL
    url = input("Please enter the YouTube live stream URL: ")
    
    # Capture chat data using app.py
    chat_data = capture_chat_data(url)
    
    # Connect to MongoDB and get the collection using db.py
    db = get_database_connection()
    collection = db.get_collection("test3")
    collection.create_index([("message_id", 1)], unique=True)  # Ensure unique message IDs
    
    # Insert chat data into MongoDB
    for document in chat_data:
        try:
            insert_document(collection, document)
        except Exception as e:
            print(f"Error inserting message with ID {document['message_id']}: {e} \n")
            break

    # Optional: Further processing or analysis using analytics.py
    # results = <Call to any function in analytics.py>
    # print(results)
    print(get_hype_moments(get_moments(collection)))



if __name__ == "__main__":
    main()
#try storing url as well, and comparing url to see if needs to access the api or not to save time