import pickle

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from os.path import exists

scopes = ['https://www.googleapis.com/auth/calendar.readonly']

def authenticate_user():
    if exists("../credentials/token.pkl"):
        print("--------------------------------------------")
        print("--- User Authenticate Already Performed ----")
        print("--------------------------------------------")
    else:
        flow = InstalledAppFlow.from_client_secrets_file('..//credentials//client_secret.json', scopes=scopes)
        credentials = flow.run_console()
        pickle.dump(credentials, open("../credentials/token.pkl", "wb"))

def get_authenticated_user():
    credentials = pickle.load(open("../credentials/token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)
    return service