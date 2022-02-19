import pytesseract
from PIL import Image

def image_2_text(file):
    img = Image.open(file);
    res = pytesseract.image_to_string(img);

    return res;