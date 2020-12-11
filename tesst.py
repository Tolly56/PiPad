import pytesseract
from PIL import Image

img = Image.open("test.png")
text = pytesseract.image_to_string(img, config ='--psm 6')
print(text)