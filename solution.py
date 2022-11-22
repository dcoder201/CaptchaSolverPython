from PIL import Image
import pytesseract
import numpy as np
import base64

img_base64 = driver.execute_script("""
    var ele = arguments[0];
    var cnv = document.createElement('canvas');
    cnv.width = ele.width; cnv.height = ele.height;
    cnv.getContext('2d').drawImage(ele, 0, 0);
    return cnv.toDataURL('image/jpeg').substring(22);    
    """, driver.find_element(By.XPATH,"provide Full Xpath of captcha element here"))
with open(r"image.jpg", 'wb') as f:
    f.write(base64.b64decode(img_base64))


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

img_path = r"C:\Users\test.jpg"

captcha_text = pytesseract.image_to_string(Image.open(img_path))

print(captcha)
