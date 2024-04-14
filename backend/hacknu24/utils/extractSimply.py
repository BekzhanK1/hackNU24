from bs4 import BeautifulSoup
import requests

def extractSimply():

    website = 'https://www.simply.cards/'

    result = requests.get(website)

    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    formatted = soup.prettify()

    needed_divs = soup.select('div.comp-l84hzhq1.wixui-repeater div.E6jjcn span.wixui-rich-text__text')

    needed_data = [div.text for div in needed_divs]

    formatted_data = [needed_data[i] for i in range(0,len(needed_data)-1,3)]

    for index in range(len(formatted_data)):
        formatted_data[index] = formatted_data[index].replace('\n',' ')
        formatted_data[index] = formatted_data[index].replace('\u200b',' ')
        formatted_data[index] = formatted_data[index].replace('\t',' ')
        