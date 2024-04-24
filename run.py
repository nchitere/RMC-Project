# import depenencies
from flask import Flask, request, jsonify
from instance.config import Config
from app.process_data import process_data
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
    

# Endpoint to get data from MongoDB
@app.route('/get_data_from_db', methods=['GET'])
def get_data_from_db():
    try:
        data = list(collection.find())
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"message": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=True)
