from bs4 import BeautifulSoup

def extract_short_description(html: str) -> list[str]:
    """Extract the last div's text from the short description."""
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('div')[-1].get_text()


def extract_product_description(html: str) -> list[str]:
    """Extract the text from the first div with class 'col-md-11'."""
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all("div", class_="col-md-11")[0].get_text()


def clean_and_extract_table(html: str) -> str:
    """Clean the HTML by removing <small> tags and class attributes, then return the table."""
    soup = BeautifulSoup(html, 'html.parser')
    
    for small_tag in soup.find_all("small"):
        small_tag.unwrap()

    for tag in soup.find_all(True):
        del tag["class"]

    table = soup.find("table")
    return str(table)


def extract_h3_content(html) -> str:
    """Extract all text from <h3> tags and return as a comma-separated string."""
    soup = BeautifulSoup(html, 'html.parser')
    h3_tags = soup.find_all("h3")
    return ", ".join([h3.get_text() for h3 in h3_tags])