
from app.db_operations import DbOperations

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
        "recommend_this_facility": data.get("Would_recommend_this_facility"),
        "areas_to_improve": data.get("_22a_From_your_personal_experi")
    }
    return formatted_fields

def save_to_db(processed_data):
    db_operations = DbOperations('kakamega_rmc')
    db_operations.save_one_to_db(processed_data)



def process_data(data):
    processed_data = extract_fields(data)
    save_to_db(processed_data)
    return processed_data
    