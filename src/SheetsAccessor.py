import json
import requests

from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
from google.oauth2 import service_account

def get_oauth_access():
    SCOPES = "https://www.googleapis.com/auth/spreadsheets"
    SERVICE_ACCOUNT_FILE = "./src/not_service.json"
    
    flow = InstalledAppFlow.from_client_secrets_file(SERVICE_ACCOUNT_FILE, SCOPES)
    flow.run_local_server()
    credentials = flow.credentials
    spreadsheet = googleapiclient.discovery.build('sheets','v4',credentials=credentials)
    return spreadsheet

# We have the OAUTH creds for python, we need to snatch a key
# We also need to get all of the CSV info from the sheet
def get_spreadsheet_info_as_json(spreadsheet):
    # I dont want to log in all the time, lets cache the auth token...
    # We'll have to do the selenium shit again...
    # Lets also read the OAUTH info from a JSON so we dont expose it on github...
    # Read the client json :)
    

    #TODO: Dynamic sheet names, dynamic sheet ranges
    sheet_id = "1TdRKfhyk3bKiFSFvoTiG52SMB8n00LhVUQsimarWHHk"    
    sheet_range = "Sheet1!C2:F3036"

    spreadsheet_items = spreadsheet.spreadsheets().values().get(spreadsheetId = sheet_id, range = sheet_range).execute()
    return spreadsheet_items["values"]

# We need to get the cards from all of the decks in anki
def get_deck_info_as_json(deck_name):
    pass

# As prep, we should reformat the spreadsheet and consolidate ALL of the deck categories into the Everything Deck
# Actually, we wont even Need the everything deck... just the main column and sorted column...

# ---There are two main things we need to do---
# ---ONE: We should check to make sure the Everything Deck cards are saturated from the spreadsheet
# We need to cross check the cards with the spreadsheet entries, how?
# Every card will have 2 versions, a normal and a swapped version.
# We should try to map each spreadsheet entry to two cards then. 
def check_everything_deck_saturation():
    pass

# ---TWO: We should check to make sure every 2k/6k Deck card is in the spreadsheet
# Easy... get active cards and check the spreadsheet for the matching entrys.
# If an entry is not found, check for the closest one by finding the Edit distance on the kanji, kana, and definition
# Print every card that does not have a spreadsheet entry, and the closest match

# There should be an option to forcefully add any card that does not have an entry.
# When we add cards, also push them to the Everything Deck column.
def check_spreadsheet_saturation():
    pass

spreadsheet_access = get_oauth_access()
spreadsheet_data = get_spreadsheet_info_as_json(spreadsheet_access)