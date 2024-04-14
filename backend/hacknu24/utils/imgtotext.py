from os import path
import pytesseract
from PIL import Image

# the default 
def convert_img_to_text(image_path):
    current_dir = path.dirname(path.abspath(__file__))
    file_path = path.join(current_dir, '../images', image_path)
    
    image_file = Image.open(file_path) 
    image_file.save(file_path, quality=200)

    return pytesseract.image_to_string(Image.open(file_path), lang='eng', config='--psm 10')


