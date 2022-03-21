from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

import pickle

scopes = ['https//www.googleapis.com/auth/calendar']

def authenticate_user():
    flow = InstalledAppFlow.from_client_secrets_file('..//credentials//client_secret.json', scopes=scopes)
    flow.run_console()
    pickle.dump(credentials, open("..//credentials//token.pkl", "wb"))

def get_authenticated_user():
    credentials = pickle.load(open("..//credentials//token.pkl", "rb"))