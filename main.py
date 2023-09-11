# from db import get_database_connection, insert_document
# from analytics import get_hype_moments, get_moments
# from pymongo.errors import DuplicateKeyError
# import json



from app import capture_chat_data
from db import get_database_connection, insert_document
from analytics import get_hype_moments, get_moments
def main():
    # db = get_database_connection()
    # collection = db.get_collection("Live-Chat-Data")
    # collection.create_index([("message_id", 1)], unique=True)

    # new_document = {
    #     "name": "John",
    #     "age": 30,
    #     "city": "New York"
    # }

    # insert_document(collection, new_document)




    # f = open("./jsons/chat2.json", "r", encoding='utf-8')
    # data = json.load(f)

    

    # for message in data:

        # document = {
        #     "message_id": message["message_id"], 
        #     "name": message['author']['name'],
        #     'message': message['message'],
        #     "time_stamp": message['time_text'],
        #     "time_in_seconds": message["time_in_seconds"],
        # } 
    #     try:
    #         insert_document(collection, document)
    #         # collection.insert_one(document)
    #     except DuplicateKeyError:
    #         print("Error: Duplicate message ID. This message ID already exists in the collection.")




    # print(get_hype_moments(get_moments(collection)))




    # for message in data:
    #     document = {
    #         "name": message['author']['name'],
    #         'message': message['message'],
    #         "time_stamp": message['time_text']
    #     } 
    #     insert_document(collection, document)
        








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
            print(f"Error inserting message with ID {document['message_id']}: {e}")
    
    # Optional: Further processing or analysis using analytics.py
    # results = <Call to any function in analytics.py>
    # print(results)
    print(get_hype_moments(get_moments(collection)))






if __name__ == "__main__":
    main()
