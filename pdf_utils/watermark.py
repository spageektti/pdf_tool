import PyPDF2

def add_watermark(input_pdf, output_pdf, watermark_pdf):
    """Add a watermark to each page of the input PDF."""
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    watermark_reader = PyPDF2.PdfReader(watermark_pdf)
    watermark_page = watermark_reader.pages[0]

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)
    print(f"Added watermark from {watermark_pdf} to {input_pdf}, saved as {output_pdf}")
