import pytesseract
from PIL import Image, ImageOps, ImageEnhance
import re

def image_2_text(file, language):
    img = Image.open(file);

    # pytesseract extracts the text
    res = process_text(pytesseract.image_to_string(proc_img, lang=language));
    img.close();
    return res;

# this uses a bunch of methodes to insure to get most words
# turns to lower case, there will be only one word, removes special characters
def image_2_words(file, language):
    img = Image.open(file);
    img = img.convert('RGB');

    # Standard
    text = pytesseract.image_to_string(img, lang=language)
        
    # GreyScale
    grey_img = ImageOps.grayscale(img);
    text = text + ' ' + pytesseract.image_to_string(grey_img, lang=language);

    # Invert
    inv_base_img = ImageOps.invert(img);
    text = text + ' ' + pytesseract.image_to_string(inv_base_img, lang=language);

    # Auto Contrast
    auto_con_base_img = ImageOps.autocontrast(img);
    text = text + ' ' + pytesseract.image_to_string(auto_con_base_img, lang=language);
    auto_con_grey_img = ImageOps.autocontrast(grey_img);
    text = text + ' ' + pytesseract.image_to_string(auto_con_grey_img, lang=language);

    # Hard Processing the Image
    # proc_img = ImageEnhance.Sharpness(grey_img).enhance(2);
    proc_img = ImageEnhance.Contrast(grey_img).enhance(10.0);
    proc_img = ImageEnhance.Brightness(proc_img).enhance(0.6);
    text = text + ' ' + pytesseract.image_to_string(proc_img, lang=language);

    res = ready_text(text);
    
    proc_img.close();
    auto_con_base_img.close();
    auto_con_grey_img.close();
    grey_img.close();
    inv_base_img.close();
    img.close();

    return res;

def process_text(text):
    res = text.replace('\n',' ').replace('\x0c','').replace('\t',' ').replace('  ',' ');
    res = res.strip();

    return res;

def ready_text(text):
    res = process_text(text);

    #strip special characters
    res = re.sub("[^A-Za-z0-9']+", ' ', res).replace('  ', ' ');
    res = res.lower();

    #insure single instance of each word
    arr = res.split(' ');

    word_set = {''}
    out = '';
    for word in arr:
        if word not in word_set:
            out = out + ' ' + word;
            word_set.add(word);

    out = out.strip();
    return out;