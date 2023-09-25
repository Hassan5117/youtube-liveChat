from flask import Flask, jsonify, request
from flask_cors import CORS

from app import capture_chat_data
from db import get_database_connection, insert_document
from analytics import get_hype_moments, get_moments

app = Flask(__name__)
CORS(app)  # This allows for cross-origin requests

@app.route('/api/mainCOPY', methods=['POST'])
def get_greeting():
    data = request.json

    # Prompt user for YouTube live stream URL
    # url = input("Please enter the YouTube live stream URL: ")
    
    # Capture chat data using app.py
    url = data.get('input')
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
    results = get_hype_moments(get_moments(collection))
    return jsonify(message=results)

if __name__ == '__main__':
    app.run(debug=True)


#try storing url as well, and comparing url to see if needs to access the api or not to save time