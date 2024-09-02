import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup

from sheets import authenticate_with_google, update_google_sheet
from manipulation import (
    extract_short_description,
    extract_product_description,
    clean_and_extract_table,
    extract_h3_content
)


if __name__ == "__main__":
    # Define constants
    creds_file = "sheetsprocessor-434314-abed63ad281d.json"
    sheet_name = "test"

    # Authenticate and open the sheet
    sheet = authenticate_with_google(creds_file, sheet_name)

    # Get all values in the sheet
    try:
        data = sheet.get_all_records()
    except gspread.exceptions.GSpreadException as e:
        print("Ensure the headers does not already exist in the sheets.")
        raise
    
    # Extract and update Google sheets
    new_short_description = extract_short_description(data[0]['SOURCE Short Description'])
    update_google_sheet(sheet, 2, 10, "NEW Short Description", new_short_description)

    new_product_description = extract_product_description(data[0]['SOURCE product_description'])
    update_google_sheet(sheet, 2, 11, "NEW product_description", new_product_description)

    cleaned_table = clean_and_extract_table(data[0]['SOURCE product_description'])
    update_google_sheet(sheet, 2, 12, "NEW specs table", cleaned_table)

    new_content_list = extract_h3_content(data[0]['SOURCE Content'])
    update_google_sheet(sheet, 2, 13, "NEW Content", new_content_list)