import pyautogui
import cv2
import numpy
import PIL
from PIL import Image
import pytesseract



# If you don't have tesseract executable in your PATH, include the following:

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Natha\OneDrive - emporia.edu\Class_Project_New\Tesseract-OCR\tesseract.exe"

# Simple image to string
print(pytesseract.image_to_string(Image.open('Screenshot_1.png')))
#print(pytesseract.image_to_string(Image.open('Screenshot_2.png')))

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open('Screenshot_1.png')))
#print(pytesseract.image_to_boxes(Image.open('Screenshot_2.png')))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open('Screenshot_1.png')))
#print(pytesseract.image_to_data(Image.open('Screenshot_2.png')))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open('Screenshot_1.png')))
#print(pytesseract.image_to_osd(Image.open('Screenshot_2.png')))

# In order to bypass the internal image conversions, just use relative or absolute image path
# NOTE: If you don't use supported images, tesseract will return error
print(pytesseract.image_to_string('Screenshot_1.png'))
#print(pytesseract.image_to_string('Screenshot_2.png'))

# get a searchable PDF
#pdf = pytesseract.image_to_pdf_or_hocr('Screenshot_1.png', extension='pdf')
#pdf = pytesseract.image_to_pdf_or_hocr('Screenshot_2.png', extension='pdf')

# get HOCR output
#hocr = pytesseract.image_to_pdf_or_hocr('Screenshot_1.png', extension='hocr')
#hocr = pytesseract.image_to_pdf_or_hocr('Screenshot_2.png', extension='hocr')

