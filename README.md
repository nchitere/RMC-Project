# RMC-Project
## Project: Respectful Maternity Care Data Collection with Flask and MongoDB

### Overview
This Flask project aims to handle data collected on respectful maternity care in selected facilities in Kakamega County using the KoboToolbox platform. The collected data will be stored in a MongoDB database for further analysis and reporting.

### Dependencies
- Flask: Web framework for building the API endpoints.
- instance.config: Configuration file for app settings.
- app.process_data: Module for processing incoming data.
- app.db_operations: Module for interacting with the MongoDB database.
- json: Library for handling JSON data.
- bson: Library for working with BSON data types in MongoDB.

### Setup
1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Configure the MongoDB connection details in `instance.config`.
3. Run the Flask application by executing `python app.py`.

### Endpoints
1. **POST /receive_data_from_kobo**
   - Description: Receives data from KoboToolbox, processes it, and inserts it into MongoDB.
   - Response:
     - 200: Data successfully processed and inserted.
     - 400: No data received.
     - 500: Error during data processing or insertion.

2. **GET /get_data_from_db**
   - Description: Retrieves data from the MongoDB database.
   - Response:
     - 200: Data retrieved successfully.
     - 404: No data found in the database.
     - 500: Error during data retrieval.

### Usage
1. Send POST requests to `/receive_data_from_kobo` with data from KoboToolbox to store in the database.
2. Access GET requests to `/get_data_from_db` to retrieve the stored data for analysis.

### Running the Application
- Ensure MongoDB is running and accessible.
- Start the Flask application by running `python app.py`.
- Access the endpoints using appropriate HTTP methods and handle the responses accordingly.

### Note
- Handle data validation and error cases to ensure the reliability and integrity of the collected data.

