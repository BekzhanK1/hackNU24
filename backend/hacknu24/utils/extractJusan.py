from bs4 import BeautifulSoup
import requests
import svg2png


def extractJusan():
    website = 'https://jusan.kz/bonus'

    result = requests.get(website)

    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    formatted = soup.prettify()

    neighbour_divs = soup.find_all('div', class_='increased-bonus_child_text__U_X2p')

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
        svg2png.convert_svg_to_png(svg)
        

    print(svg_list,png_list)



