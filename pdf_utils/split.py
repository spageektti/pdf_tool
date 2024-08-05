import PyPDF2
import os


def split_pdfs(input_pdf, output_dir, split_type, i):
    """Split a PDF either every i pages or into i parts."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_reader = PyPDF2.PdfReader(input_pdf)
    num_pages = len(pdf_reader.pages)

    if split_type == 'every':
        # Split every i pages
        for start in range(0, num_pages, i):
            pdf_writer = PyPDF2.PdfWriter()
            for page in range(start, min(start + i, num_pages)):
                pdf_writer.add_page(pdf_reader.pages[page])
            output_pdf = os.path.join(output_dir, f'part_{start // i + 1}.pdf')
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)
            print(f"Created {output_pdf}")
    elif split_type == 'parts':
        # Split into i parts
        part_size = num_pages // i
        for part in range(i):
            pdf_writer = PyPDF2.PdfWriter()
            start = part * part_size
            end = start + part_size if part < i - 1 else num_pages
            for page in range(start, end):
                pdf_writer.add_page(pdf_reader.pages[page])
            output_pdf = os.path.join(output_dir, f'part_{part + 1}.pdf')
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)
            print(f"Created {output_pdf}")
