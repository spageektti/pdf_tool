# pdf_utils/rotate.py
import PyPDF2

def rotate_pages(input_pdf, output_pdf, rotation, pages):
    """Rotate specified pages of a PDF by a given angle."""
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        if pages == 'all' or (str(page_num + 1) in pages.split(',')):
            page.rotate_clockwise(rotation)
        pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)
    print(f"Rotated pages in {input_pdf} and saved as {output_pdf}")
