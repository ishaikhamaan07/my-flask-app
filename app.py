from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


from flask import request, jsonify
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(data)

    return jsonify({
        "status": "success",
        "message": "To-Do item added successfully!"
    })



if __name__ == '__main__':
    app.run(debug=True)
