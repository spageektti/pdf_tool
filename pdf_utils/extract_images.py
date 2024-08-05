from PyPDF2 import PdfReader
from PIL import Image
import os

def extract_images(input_pdf, output_dir):
    reader = PdfReader(input_pdf)
    for page_num, page in enumerate(reader.pages):
        if '/XObject' in page['/Resources']:
            xObject = page['/Resources']['/XObject'].get_object()
            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    img_data = xObject[obj]._data
                    img_name = f'image_{page_num + 1}_{obj[1:]}.png'
                    img_path = os.path.join(output_dir, img_name)
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_data)
