import os
from pdf2image import convert_from_path
from pytesseract import image_to_string

def extract_text_from_image(image):
    text = image_to_string(image, lang='chi_tra')
    return text

def extract_text_from_pdf(file_path):
    # Convert PDF to images
    images = convert_from_path(file_path)

    # Extract text from each image
    text = ''
    for image in images:
        text += extract_text_from_image(image)

    return text

# Get the current directory path
folder_path = os.getcwd()

# Traverse the files in the directory
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(folder_path, filename)
        pdf_text = extract_text_from_pdf(file_path)

        # Create the corresponding text file
        output_file_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(pdf_text)
