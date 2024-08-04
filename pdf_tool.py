# pdf_tool.py
import argparse
from pdf_utils.merge import merge_pdfs

def main():
    parser = argparse.ArgumentParser(description="PDF manipulation tool.")
    parser.add_argument(
        '-m', '--merge',
        nargs='+',
        help='Merge specified PDF files into a single PDF. The last argument is the output file.',
        required=False
    )

    args = parser.parse_args()

    if args.merge:
        *input_pdfs, output_pdf = args.merge
        if len(input_pdfs) < 2:
            print("You need to specify at least two PDFs to merge.")
            return
        merge_pdfs(input_pdfs, output_pdf)

if __name__ == "__main__":
    main()
