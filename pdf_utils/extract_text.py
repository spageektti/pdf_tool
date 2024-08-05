import PyPDF2

def extract_text(input_pdf, output_txt):
    """Extract text from a PDF and save it to a text file."""
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    with open(output_txt, 'w') as txt_file:
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            txt_file.write(f"Page {page_num + 1}:\n{text}\n\n")
    print(f"Extracted text from {input_pdf} to {output_txt}")