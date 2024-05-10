from flask import request
from app.db_operations import DbOperations
from app.gsheet import GoogleSheetAuth

def extract_fields(data):
    formatted_fields = {
        "date_submitted": data.get("_submission_time"),
        "age": data.get("Age"),
        "consent": data.get("Consent"),
        "facility": data.get("group_bz6tp65/_3_Facility"),
        "parity": data.get("group_bz6tp65/Parity"),
        "education_level": data.get("group_bz6tp65/Educational_Level"),
        "marital_status": data.get("group_bz6tp65/Marital_status"),
        "religion": data.get("group_bz6tp65/Religion"),
        "polite_staff": data.get("Polite_staff"),
        "hcw_introduce_themselves": data.get("Did_service_providers_introduc"),
        "birth_companion": data.get("Birth_companion"),
        "insults_or_threats": data.get("Any_insults_or_threats"),
        "forced_to_do_anything": data.get("Forced_to_do_anything"),
        "procedures_explained": data.get("Procedures_explained"),
        "discriminated_against": data.get("Discriminated_against"),
        "choice_of_delivery_position": data.get("_15_Were_you_allowed_on_during_childbirth"),
        "accorded_privacy": data.get("Accorded_privacy"),
        "outcomes_explained": data.get("Explained_outcomes_examination"),
        "adequate_care_admission": data.get("_18_Do_you_feel_you_te_care_on_admission"),
        "adequate_care_labor_delivery": data.get("_19_Do_you_feel_you_g_labor_and_delivery"),
        "adequate_care_post_delivery": data.get("_20_Do_you_feel_you_care_after_delivery"),
        "professional_language": data.get("_21_Do_you_think_the_nd_friendly_language"),
        "content_with_services": data.get("_20a_Were_you_contented_with_t"),
        "reason_for_contentment":data.get("_22_1_If_Yes_in_20a_above_brie"),
        "recommend_this_facility": data.get("Would_recommend_this_facility"),
        "why_not_recommend_facility": data.get("_23_1_If_No_in_23_above_why_no"),
        "areas_to_improve": data.get("_22a_From_your_personal_experi"),
        "exact_areas_to_improve": data.get("_24_1_If_yes_in_24_above_what_")
    }
    return formatted_fields

def save_to_db(processed_data):
    db_operations = DbOperations('kakamega_rmc')
    db_operations.save_one_to_db(processed_data)

# Function to transform data into the required format for writing to googlesheets
def format_google_sheet_data(processed_data):
    transformed_entries = [[ 
                            processed_data['age'], 
                            processed_data['consent'], 
                            processed_data['facility'],
                            processed_data['parity'],
                            processed_data['education_level'],
                            processed_data['marital_status'],
                            processed_data['religion'],
                            processed_data['polite_staff'],
                            processed_data['hcw_introduce_themselves'],
                            processed_data['birth_companion'],
                            processed_data['insults_or_threats'],
                            processed_data['forced_to_do_anything'],
                            processed_data['procedures_explained'],
                            processed_data['discriminated_against'],
                            processed_data['choice_of_delivery_position'],
                            processed_data['accorded_privacy'],
                            processed_data['outcomes_explained'],
                            processed_data['adequate_care_admission'],
                            processed_data['adequate_care_labor_delivery'],
                            processed_data['adequate_care_post_delivery'],
                            processed_data['professional_language'],
                            processed_data['content_with_services'],
                            processed_data['reason_for_contentment'],
                            processed_data['recommend_this_facility'],
                            processed_data['why_not_recommend_facility'],
                            processed_data['areas_to_improve'],
                            processed_data['exact_areas_to_improve']]]
    return transformed_entries


def write_to_google_sheet(processed_data):
#     # Extract the data to create a format that will be written to the google sheet.
    google_sheet_data = format_google_sheet_data(processed_data)
#     # create an instance of the google sheet class
    google_sheet_auth = GoogleSheetAuth()
#     # Using the instance call the the "write method"
#     # Pass the correct arguments key, data & worksheet
    key = '1KDsD-akp7-qNYE0WM43ZqQ41a5R8VE1w8HgUSdnODj8'
    google_sheet_auth.write_rows_existing_sheet(google_sheet_data, key, 'RMC Data') # The write method called on the instance






def process_data(data):
    processed_data = extract_fields(data)
    save_to_db(processed_data)
    write_to_google_sheet(processed_data)
    return processed_data
    
