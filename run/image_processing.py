import pytesseract
from PIL import Image

def image_2_text(file, language):
    img = Image.open(file);
    res = pytesseract.image_to_string(img, lang=language);

    # trim string
    res = res.replace('\n',' ').replace('\x0c','');
    res = res.strip();

    return res;