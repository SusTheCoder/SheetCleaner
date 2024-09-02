import gspread
from gspread import Worksheet
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup


def authenticate_with_google(creds_file: str, sheet_name: str) -> Worksheet:
    """Authenticate with Google Sheets API and return the sheet object."""
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    try:
        client = gspread.authorize(creds)
        print("Google Sheets client has successfully been authorised.")
    except Exception as e:
        raise e
    
    return client.open(sheet_name).sheet1


def update_google_sheet(sheet: Worksheet, row: int, col: int, header: str, value: str):
    """Update the Google Sheet with the extracted data."""
    # Add header name
    sheet.update_cell(1, col, header)
    # Add data to row
    sheet.update_cell(row, col, value)

    print(f"Data has been successfully written under the column {header} in the Google Sheets.")
