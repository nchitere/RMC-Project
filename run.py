# import depenencies. ## packages installed with python takes order 
# precedence i.e math, os, json.
# This is followed by packages installed using pip
# Followed by packages within the application
import json
from bson import json_util
from flask import Flask, request, jsonify
from instance.config import Config
from app.process_data import process_data
from app.db_operations import DbOperations
from app.gsheet import GoogleSheetAuth


data = {}

# Instantiate app
app = Flask(__name__)
app.config.from_object(Config)


@app.route('/receive_data_from_kobo', methods=['POST'])
def receive_data_from_kobo():
    data = request.get_json()
    if data:  # Check if data is not empty
        try:
            data = process_data(data)
            return jsonify({"message": "Data successfully processed inserted into MongoDB"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500  # Handle insertion error
    else:
        return jsonify({"message": "No data received"}), 400  # Handle empty data case
    


@app.route('/get_data_from_db', methods=['GET'])
def get_data_from_db():
    try:
        db_ops = DbOperations('kakamega_rmc') # Replace 'collection_name' with the actual collection name
        data = db_ops.query_data_from_db()
        if data:
            # Convert BSON data types to JSON-compatible types
            
            json_data = json.loads(json_util.dumps(data, default=str))
            return jsonify(json_data), 200
        else:
            return jsonify({"message": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/read_data_from_gsheet', methods = ['GET'])
def read_data_from_gsheet():
    key = '1KDsD-akp7-qNYE0WM43ZqQ41a5R8VE1w8HgUSdnODj8'
    worksheet = 'RMC Data'
    gsheet_intance = GoogleSheetAuth()
    data = GoogleSheetAuth.read_google_worksheet(gsheet_intance,key,worksheet)
    return data



    
@app.route('/sample_end_point', methods = ['GET'])
def sample_write_to_gsheet():
    data = [
            ['actualname',1,'kajiado','Ngong'],
            ['jones',3,'nakuru','Ngong'],
            ['john',5,'narok','Ngong'],
            ['Peter',6,'kiambu','Tigoni'],
    ]
    key =  '1KDsD-akp7-qNYE0WM43ZqQ41a5R8VE1w8HgUSdnODj8'
    worksheet = 'Test'
    google_sheet = GoogleSheetAuth()
    google_sheet.write_rows_existing_sheet(data, key, worksheet)
    return {'message': 'success!'}




if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=True)
