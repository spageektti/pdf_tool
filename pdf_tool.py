import argparse
from pdf_utils.merge import merge_pdfs
from pdf_utils.split import split_pdfs
from pdf_utils.extract_text import extract_text

def main():
    parser = argparse.ArgumentParser(description="PDF manipulation tool.")
    parser.add_argument(
        '-m', '--merge',
        nargs='+',
        help='Merge specified PDF files into a single PDF. The last argument is the output file.',
        required=False
    )
    parser.add_argument(
        '-s', '--split',
        nargs=4,
        metavar=('input_pdf', 'output_dir', 'split_type', 'i'),
        help="Split a PDF. 'split_type' can be 'every' or 'parts'. 'i' is the interval or number of parts.",
        required=False
    )
    parser.add_argument(
        '-e', '--extract',
        nargs=2,
        metavar=('input_pdf', 'output_txt'),
        help="Extract text from a PDF and save it to a text file.",
        required=False
    )

    args = parser.parse_args()

    if args.merge:
        *input_pdfs, output_pdf = args.merge
        if len(input_pdfs) < 2:
            print("You need to specify at least two PDFs to merge.")
            return
        merge_pdfs(input_pdfs, output_pdf)
    
    if args.split:
        input_pdf, output_dir, split_type, i = args.split
        i = int(i)
        if split_type not in ('every', 'parts'):
            print("Invalid split_type. Use 'every' or 'parts'.")
            return
        split_pdfs(input_pdf, output_dir, split_type, i)

    if args.extract:
        input_pdf, output_txt = args.extract
        extract_text(input_pdf, output_txt)

if __name__ == "__main__":
    main()
