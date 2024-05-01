# import depenencies
from flask import Flask, request, jsonify
from instance.config import Config
from app.process_data import process_data
from app.db_operations import DbOperations
import json
from bson import json_util,ObjectId

data = {}

# Instantiate app and set up mongodb
app = Flask(__name__)
app.config.from_object(Config)




@app.route('/receive_data_from_kobo', methods=['POST'])
def receive_data_from_kobo():
    data = request.get_json()
    print(data)
    if data:  # Check if data is not empty
        try:
            processed_data = process_data(data)
            return jsonify({"message": "Data successfully processed inserted into MongoDB"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500  # Handle insertion error
    else:
        return jsonify({"message": "No data received"}), 400  # Handle empty data case
    


@app.route('/get_data_from_db', methods=['GET'])
def get_data_from_db():
    try:
        db_ops = DbOperations('kakamega_rmc')  # Replace 'collection_name' with the actual collection name
        data = list(db_ops.collection.find())
        if data:
            # Convert BSON data types to JSON-compatible types
            json_data = json.loads(json_util.dumps(data, default=str))
            return jsonify(json_data), 200
        else:
            return jsonify({"message": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=True)
