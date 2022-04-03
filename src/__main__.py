
from calendar import calendar
from multiprocessing.dummy import active_children
import sys
import pprint
import json
from unittest import result

from google_calendar_setup import *

PDF_PATH = "../templates/bth_time_report_template.pdf"
CALENDAR_PROFILES_PATH = "../profiles/calendar_profiles.json"

CALENDAR_PROFILE_NAME = "google-teaching-assistant"

PP = pprint.PrettyPrinter(indent=4)

def write_data_to_pdf():
    return 0

def read_calendar_profiles():
    # Opening JSON file
    with open(CALENDAR_PROFILES_PATH) as json_file:
        data = json.load(json_file)
    
    return data["calendars_profiles"]

def get_single_profile(profile_name):
    calendar_profiles = read_calendar_profiles()

    for profile in calendar_profiles:
        if profile_name in profile:
            return profile[profile_name]
        
    return -1

def get_calendar_id():
    profile = get_single_profile(CALENDAR_PROFILE_NAME)
    return profile["calendar_id"]

def get_calendar_item(calendar_id):
    authenticate_user()
    service = get_authenticated_user()
    result = service.calendarList().list().execute()

    for calendar_item in result["items"]:
        if calendar_item["id"] == calendar_id:
            return calendar_item

    return -1

def get_activity_key_word(activity_key_word):
    calendar_profiles = read_calendar_profiles()

    for profile in calendar_profiles:
        for profile_settings in profile.values():
            if profile_settings["activity_key_word"] == activity_key_word:
                return profile_settings["activity_key_word"]
    
    return -1

def get_events(calendar_id):
    authenticate_user()
    service = get_authenticated_user()

    events = service.events().list(calendarId=calendar_id).execute()
    return events

def get_calendar_event_names(events, activity_key_word):
    
    return_list = []
    key_word_length = len(activity_key_word)

    for event_entry in events['items']:
        if activity_key_word == event_entry["summary"][:key_word_length]:
            return_list.append(event_entry['summary'])
        

    return return_list, events

def get_event_times(event_name_list):
    return 0

def read_data_from_calendar():
    
    calendar_id = get_calendar_id()
    activity_key_word = get_activity_key_word("TA:")
    
    if get_calendar_item(calendar_id) == -1:
        print("Failed to get calendar_item with calendar_id: ", calendar_id)
        sys.exit(-1)

    events = get_events(calendar_id)
    
    event_name_list = get_calendar_event_names(events, activity_key_word)

    
    

    

def read_user_profile():
    return 0

def read_template():
    return 0

def main() -> int:
    read_data_from_calendar()

    return 0

if __name__ == "__main__":
    sys.exit(main())