import pytesseract
from PIL import Image
import pdfplumber


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Dell\Documents\tesseract.exe"



def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_pdf(file_path)
    else:
        return extract_image(file_path)



def extract_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text



def extract_image(path):
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    return text