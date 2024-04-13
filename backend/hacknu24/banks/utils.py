from bs4 import BeautifulSoup
import requests
import re

def clean_text(text):
    """ Helper function to clean unwanted special characters from the text, including non-breaking spaces and zero-width spaces. """
    text = re.sub(r'\s+', ' ', text)  # Replace all whitespace characters with a single space
    text = text.replace('\xa0', ' ')  # Explicitly replace non-breaking spaces
    text = text.replace('\u200b', '')  # Remove zero-width spaces
    return text.strip()

def get_element_texts(elements, skip_alternate=False):
    """ Helper function to extract text from a list of elements, optionally skipping alternate elements. """
    if skip_alternate:
        # Take only elements at even indices (0, 2, 4, ...)
        filtered_elements = [clean_text(elements[i].text) for i in range(len(elements)) if i % 2 == 0]
    else:
        filtered_elements = [clean_text(element.text) for element in elements]
    return filtered_elements

def is_valid_address(text):
    """ Check if the text is likely to be a valid address and not an unwanted string. """
    invalid_keywords = ['реклама', 'филиалов', 'филиала', 'ооо', 'акция', '*ао', 'тоо', 'филиал', 'ао', 'ип']
    return not any(keyword in text.lower() for keyword in invalid_keywords)

def find_places(city, place):
    """ Function to find places in a given city with the provided place name. Returns a list of entries. """
    # List to hold all the dictionaries of entries
    entries = []
    # Construct the URL with the input place
    url = f"https://2gis.kz/{city}/search/{place}" 
    print(url)

    # Headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    # Send the HTTP request
    response = requests.get(url, headers=headers)

    # Check the status code to ensure the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all relevant elements
        names = soup.find_all('span', class_='_1al0wlf')
        names_texts = get_element_texts(names)

        span_elements = soup.find_all('span', class_='_oqoid')
        category_texts = get_element_texts(span_elements)

        streets = soup.find_all('span', class_='_1w9o2igt')
        street_texts = get_element_texts(streets)  # Apply skipping logic

        street_index = 0  # Initialize street index
        # Process and pair data
        for name_text, category_text in zip(names_texts, category_texts):
            found_valid_street = False
            while street_index < len(street_texts):
                if is_valid_address(street_texts[street_index]):
                    entries.append({'name': name_text, 'category': category_text, 'street': street_texts[street_index]})
                    street_index += 1  # Move to the next street text only if a valid one was used
                    found_valid_street = True
                    break
                street_index += 1  # Skip invalid street
            if not found_valid_street:  # No valid street was found for this pair
                entries.append({'name': name_text, 'category': category_text, 'street': 'No valid street found'})

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return entries

