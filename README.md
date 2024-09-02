# 📝 Google Sheets Data Processor

This project is designed to read data from a Google Sheet, process and clean the HTML content within the cells, and write the cleaned data back into the Google Sheet. The processing involves extracting specific content from the HTML, such as text from `<h3>` tags, removing unwanted tags, and handling table data.

## Features

- **Read Data:** Retrieve data from a specified Google Sheet.
- **Process HTML Content:** Clean and extract meaningful content from HTML strings in the sheet.
- **Write Data:** Insert the cleaned and processed data back into the Google Sheet, optionally in new columns.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- A Google Cloud project with a service account enabled for Google Sheets API and Google Drive API.
- A JSON key file from your Google Cloud service account for authentication.

### Dependencies

Install the required Python libraries using pip:

```bash
pip install beautifulsoup4 gspread oauth2client
```

## Project Structure
- main.py: The main script that contains the logic for reading, processing, and writing the data.
- sheetsprocessor-434314-abed63ad281d.json: The JSON key file for Google API authentication (replace with your actual file).

## Usage
1. Clone the repository (if applicable):
```bash
Copy code
git clone https://github.com/your-username/google-sheets-data-processor.git
cd google-sheets-data-processor
```
2. Update the Credentials:

Replace sheetsprocessor-434314-abed63ad281d.json with your actual JSON key file.

3. Modify the Script (if necessary):

The script processes the first row in the Google Sheet. If you need to process more rows, adjust the code accordingly.
Run the Script:

4. Execute the script to process the data:

```
python main.py
```
This will read the Google Sheet, clean the HTML content, and write the processed data back into new columns.

## Functionality
### Authentication
The script uses OAuth2 to authenticate with the Google Sheets API and Google Drive API.

### Data Processing
- Short Description: Extracts the content of the last `<div>` tag in the "SOURCE Short Description" column.
- Product Description: Extracts the content of the first `<div>` tag with class col-md-11 in the "SOURCE product_description" column.
- Table Data: Cleans the HTML table in the "SOURCE product_description" column by removing `<small>` tags and class attributes.
- Content Extraction: Extracts all `<h3>` tag content in the "SOURCE Content" column and compiles it into a comma-separated string.

## Output
The processed data is written back to the Google Sheet in new columns titled "NEW Short Description", "NEW product_description", "NEW specs table", and "New Content".

## License
This project is licensed under the MIT License - see the LICENSE file for details.