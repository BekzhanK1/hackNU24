from os import path
import convertapi

convertapi.api_secret = 'sCtWU5thm9FqWuN6'

def convert_svg_to_png(image):
    current_dir = path.dirname(path.abspath(__file__))
    file_path = path.join(current_dir, '../images', image)

    convertapi.convert('png', {
        'File': file_path
    }, from_format = 'svg').save_files('../images')