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

# 使用範例：
pdf_file_path = "/Users/oscarchen/Documents/Fun/PDF_WORD compare/oscar_cv_2023.pdf"
pdf_text = extract_text_from_pdf(pdf_file_path)

output_file_path = "/Users/oscarchen/Documents/Fun/PDF_WORD compare/oscar_cv_2023.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(pdf_text)
