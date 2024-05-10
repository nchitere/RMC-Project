# RMC-Project
## Project: Respectful Maternity Care Data Collection with Flask and MongoDB

### Overview
This Flask project aims to handle data collected on respectful maternity care in selected facilities in Kakamega County using the KoboToolbox platform. The collected data will be stored in a MongoDB database for further analysis and reporting. A copy of the data will be availble to the researchers on google sheet.
Here is the general project layout
├──RMC-PROJECT
    ├──📁 app
    │	├──📄 db_operations.py
    │	├──📄 googledrive.py
    │	├──📄 gsheet.py
    │	├──📄 process_data.py
    │	├──📁 __pycache__
    │	│	├──📄 db_operations.py
    │	│	├──📄 gsheet.py
    │	│	├──📄 process_data.py
    ├───📁 instance
        ├──__pycache__
        ├──config.py
    ├──📁 venv
    ├──📄 credentials.json
    ├──📄 gd_credentials.json
    ├──📄 README.md
    ├──📄 requirements.txt
    ├──📄 run.py
  
### Folders
1. instance
The config.py module has class and methods that configure the connection to 
MongoDB during development and later on deployment


2. app
2a. db_operations.py
    The class DbOperations has instances and methods to handle MongoDB Database
    The class constructor(def__init__()) has instances that handle connection to the database and it collection. It ensures the required resources are available for the class methods to operate on.
    One of methods under DbOperations are def_save_one_db() that user the insert_one() method to insert an individual entry into MongoDB(RMC)
    The other method is def_query_data_from_db(). It uses find() method to query data from MongoDB(RMC)

2b. gsheet.py
    The class GoogleSheetAuth has instances and methods to handle authorization and operations on google sheet. It uses credentials in the file credentials.json
    The consturtor(def__init__()) ensures the methods have access to credentials to allow for their operation.
    The methods to 
      I. Authorize access google sheet(def authorize_account())
      II.Open google sheet(def open_sheet())
      III.Read google sheet(def read_google_worksheet())
      IV. Write to google sheet(def write_rows_existing_sheet())
      
2c. process_data.py
    The module process the data into the desired format including column labels
    I. Function def extract_fields() is used for mapping the correct column labels.
    II. Function def save_to_db() saves the processed data to MongoDB
    III. Function def format_google_sheet_data() formats the data into the structure that can be written to the googlesheet.
    IV. Function def write_to_google_sheet() writes data to googlesheet
    V. Function def process_data() process the data by calling the above functions
    
2d. googledrive.py



### Windows Setup
1. A repository created on github
2. The repo cloned on the rmc-project directory using git clone
3. A virtual environment instantiate(python -m venv venv) and activated (venv\Scripts\activate)
4. Folder/file structure created

### To run locally
1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Configure the MongoDB connection details in `instance.config`.
3. Run the Flask application by executing `python run.py`.

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
- Start the Flask application by running `python run.py`.
- Access the endpoints using appropriate HTTP methods and handle the responses accordingly.

### Note
- Handle data validation and error cases to ensure the reliability and integrity of the collected data.

