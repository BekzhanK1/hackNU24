from bs4 import BeautifulSoup
import requests
import re
from os import path
import os
from .models import CashbackOffer
import convertapi
from PIL import Image
import pytesseract

convertapi.api_secret = 'sCtWU5thm9FqWuN6'


def clean_text(text):
    """ Helper function to clean unwanted special characters from the text, including non-breaking spaces and zero-width spaces. """
    text = re.sub(
        r'\s+', ' ', text)  # Replace all whitespace characters with a single space
    text = text.replace('\xa0', ' ')  # Explicitly replace non-breaking spaces
    text = text.replace('\u200b', '')  # Remove zero-width spaces
    return text.strip()


def get_element_texts(elements, skip_alternate=False):
    """ Helper function to extract text from a list of elements, optionally skipping alternate elements. """
    if skip_alternate:
        # Take only elements at even indices (0, 2, 4, ...)
        filtered_elements = [clean_text(elements[i].text)
                             for i in range(len(elements)) if i % 2 == 0]
    else:
        filtered_elements = [clean_text(element.text) for element in elements]
    return filtered_elements


def is_valid_address(text):
    """ Check if the text is likely to be a valid address and not an unwanted string. """
    invalid_keywords = ['реклама', 'филиалов', 'филиала',
                        'ооо', 'акция', '*ао', 'тоо', 'филиал', 'ао', 'ип']
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
                    entries.append(
                        {'name': name_text, 'category': category_text, 'street': street_texts[street_index]})
                    street_index += 1  # Move to the next street text only if a valid one was used
                    found_valid_street = True
                    break
                street_index += 1  # Skip invalid street
            if not found_valid_street:  # No valid street was found for this pair
                entries.append(
                    {'name': name_text, 'category': category_text, 'street': 'No valid street found'})

    else:
        print(
            f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return entries


def convert_svg_to_png(image):
    current_dir = path.dirname(path.abspath(__file__))
    file_path = path.join(current_dir, '../images', image)

    try:
        res = convertapi.convert('png', {
            'File': file_path
        }, from_format='svg').file.save(file_path)
    except:
        return KeyError

    file_name = file_path.split('.')[2].split('/')
    print(file_name, res)
    file_name = file_name[2]

    return file_name + ".png"


# the default
def convert_img_to_text(image_path):
    current_dir = path.dirname(path.abspath(__file__))
    file_path = path.join(current_dir, '../images', image_path)
    print("img to text", file_path)

    image_file = Image.open(file_path)
    image_file.save(file_path, quality=200)

    return pytesseract.image_to_string(Image.open(file_path), lang='eng', config='--psm 10')


def extractJusan():
    website = 'https://jusan.kz/bonus'

    result = requests.get(website)

    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    formatted = soup.prettify()

    neighbour_divs = soup.find_all(
        'div', class_='increased-bonus_child_text__U_X2p')

    texts = soup.select('div.increased-bonus_child_text__U_X2p > p')

    texts = [texts[i].text for i in range(len(texts)) if i % 3 == 0]

    print(texts)

    parent_divs = [neighbour.parent for neighbour in neighbour_divs]

    links = [parent.contents[0]['src'] for parent in parent_divs]

    svg_list = []
    png_list = []
    for link in links:
        start = link.find('https://')
        if '.svg' in link:
            end = link.find('.svg')+4
            svg_list.append(link[start:end])
        else:
            end = link.find('.png')+4
            png_list.append(link[start:end])

    for svg in svg_list:
        convert_svg_to_png(svg)

    print(svg_list)

    return [texts, svg_list]


def extractSimply():

    website = 'https://www.simply.cards/'

    result = requests.get(website)

    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    formatted = soup.prettify()

    needed_divs = soup.select(
        'div.comp-l84hzhq1.wixui-repeater div.E6jjcn span.wixui-rich-text__text')

    needed_data = [div.text for div in needed_divs]

    formatted_data = [needed_data[i] for i in range(0, len(needed_data)-1, 3)]

    for index in range(len(formatted_data)):
        formatted_data[index] = formatted_data[index].replace('\n', ' ')
        formatted_data[index] = formatted_data[index].replace('\u200b', ' ')
        formatted_data[index] = formatted_data[index].replace('\t', ' ')


def jusanScrape():

    current_dir = path.dirname(path.abspath(__file__))
    folder_path = path.join(current_dir, '../images')

    [categories, svg_list] = extractJusan()
    # len_category = len(categories) - 1
    k = 0

    for i, svg in enumerate(svg_list):
        if 'https://' in svg:
            data = requests.get(svg).text
            if k < len(categories):
                filename = categories[k].replace(
                    '/', '_').replace('\\', '_').replace(':', '_')

            # Construct the file destination path
                file_dest = path.join(folder_path, f'{filename}.svg')

                with open(file_dest, 'w') as file:
                    file.write(data)
                k += 1
            else:
                break

    for i, file in enumerate(os.listdir(folder_path)):
        if file.endswith('.svg'):
            print("I am svg file", file)
            file_name = convert_svg_to_png(file)
            cashback_value = convert_img_to_text(file_name)

            category = categories[i]
            print(category)
            cashback_offer = CashbackOffer(
                category=category, cashback=cashback_value, bank=2)

            cashback_offer.save()
