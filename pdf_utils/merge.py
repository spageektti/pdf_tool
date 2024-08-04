import PyPDF2

def merge_pdfs(pdf_list, output):
    """Merge multiple PDFs into a single PDF."""
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        try:
            pdf_reader = PyPDF2.PdfReader(pdf)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
        except Exception as e:
            print(f"Error processing {pdf}: {e}")
            return

    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    print(f"Merged PDFs into {output}")
