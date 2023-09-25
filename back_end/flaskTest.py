from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows for cross-origin requests

@app.route('/api/greeting', methods=['GET'])
def get_greeting():
    return jsonify(message="Hello from Flask! Edited")

if __name__ == '__main__':
    app.run(debug=True)
