import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def extract_text_from_pdf(file_path):
    resource_manager = PDFResourceManager()
    output_string = StringIO()
    codec = 'utf-8'
    laparams = LAParams(line_margin=0.1)
    converter = TextConverter(resource_manager, output_string, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(file_path, 'rb') as file:
        for page in PDFPage.get_pages(file):
            interpreter.process_page(page)

    text = output_string.getvalue()
    converter.close()
    output_string.close()
    return text

# 取得當前的資料夾路徑
folder_path = os.getcwd()

# 遍歷資料夾內的檔案
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(folder_path, filename)
        pdf_text = extract_text_from_pdf(file_path)

        # 建立對應的文字檔案
        output_file_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(pdf_text)
