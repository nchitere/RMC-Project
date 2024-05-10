from datetime import datetime
import gspread
#from oauth2client.service_account import ServiceAccountCredentials. Did not work
from instance.config import AppConfig
import logging
# from google.oauth2.service_account import Credentials
from google.oauth2 import service_account



class GoogleSheetAuth:
    """class that handles google sheet
    auth
    """

    def __init__(self):
        self.account_credentials = f"{AppConfig.BASE_DIR}/credentials.json"

    def authorize_account(self):
        """Provides authorization to a particular spreadsheet on google drive
        :returns: the worksheet instance
        """
        credentials_file = self.account_credentials
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        # credentials = service_account.Credentials.from_service_account_file(
        #     credentials_file, scope)
        credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scope)
        google_auth = gspread.authorize(credentials)

        return google_auth
    
    def open_sheet(self, sheet_key):
        """Function that opens particular sheet in
        the drive
        Args:
            sheet_key(str): google sheet key
        """
        google_auth = self.authorize_account()
        return google_auth.open_by_key(sheet_key)
    
    # def read_google_sheet(self, key):
    #     """Function that retries helpdesk schedules records
    #     Returns:
    #         schedules_records(dict): all schedules records
    #     """
    #     try:
    #         google_sheet = self.open_sheet(
    #             key
    #         )

    #         #read specific row
    #         working_sheet = google_sheet.worksheet('RMC Data')
    #         schedules_records = working_sheet.get_all_records()
    #         return schedules_records

    #     except Exception as error:
    #         logging.error(error)

    def read_google_worksheet(self, key, worksheet):
        """Function that writes records from gsheet
        Returns:
            a copy of records submitted through kobo:
        """
        try:
            google_sheet = self.open_sheet(
                key
            )

            #read specific row
            working_sheet = google_sheet.worksheet(worksheet)
            schedules_records = working_sheet.get_all_records()
            return schedules_records

        except Exception as error:
            logging.error(error)

    def write_rows_existing_sheet(self, data, key, worksheet):
        """Method that writes data to existing google sheet
        sample data = [['gg', '1', 'Kakamega', 'likuyani'],[]]
        key = 1KDsD-akp7-qNYE0WM43ZqQ41a5R8VE1w8HgUSdnODj8
        worksheet = Test
        """

        try:
            # authorize and open the google sheet
            google_sheet = self.open_sheet(
                key
            )
            worksheets = [work_sheet.title for work_sheet in google_sheet.worksheets()]
            if worksheet not in worksheets:
                self.create_work_sheet(google_sheet, worksheet, key)

            working_sheet = google_sheet.worksheet(worksheet)
            working_sheet.append_rows(data, value_input_option='RAW')

        except Exception as error:
            logging.error(error)    