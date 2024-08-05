import argparse
from pdf_utils.merge import merge_pdfs
from pdf_utils.split import split_pdfs
from pdf_utils.extract_text import extract_text
from pdf_utils.rotate import rotate_pages
from pdf_utils.watermark import add_watermark
from pdf_utils.encrypt import encrypt_pdf
from pdf_utils.extract_images import extract_images
from pdf_utils.images_to_pdf import images_to_pdf

def main():
    parser = argparse.ArgumentParser(description="PDF manipulation tool")
    subparsers = parser.add_subparsers(dest='command')

    # Merge PDFs
    merge_parser = subparsers.add_parser('-m', '--merge', help="Merge PDF files")
    merge_parser.add_argument('input_pdfs', nargs='+', help="Input PDF files")
    merge_parser.add_argument('output_pdf', help="Output PDF file")

    # Split PDFs
    split_parser = subparsers.add_parser('-s', '--split', help="Split a PDF file")
    split_parser.add_argument('input_pdf', help="Input PDF file")
    split_parser.add_argument('output_dir', help="Output directory")
    split_parser.add_argument('split_type', choices=['every', 'parts'], help="Split type: 'every' to split every i pages, 'parts' to split into i parts")
    split_parser.add_argument('i', type=int, help="Number of pages or parts")

    # Extract Text
    extract_parser = subparsers.add_parser('-e', '--extract-text', help="Extract text from a PDF file")
    extract_parser.add_argument('input_pdf', help="Input PDF file")
    extract_parser.add_argument('output_txt', help="Output text file")

    # Rotate Pages
    rotate_parser = subparsers.add_parser('-r', '--rotate', help="Rotate pages in a PDF file")
    rotate_parser.add_argument('input_pdf', help="Input PDF file")
    rotate_parser.add_argument('output_pdf', help="Output PDF file")
    rotate_parser.add_argument('rotation', type=int, choices=[90, 180, 270], help="Rotation angle")
    rotate_parser.add_argument('pages', help="Pages to rotate (comma-separated) or 'all'")

    # Add Watermark
    watermark_parser = subparsers.add_parser('-w', '--watermark', help="Add a watermark to a PDF file")
    watermark_parser.add_argument('input_pdf', help="Input PDF file")
    watermark_parser.add_argument('output_pdf', help="Output PDF file")
    watermark_parser.add_argument('watermark_pdf', help="Watermark PDF file")

    # Encrypt PDF
    encrypt_parser = subparsers.add_parser('-p', '--encrypt', help="Encrypt a PDF file")
    encrypt_parser.add_argument('input_pdf', help="Input PDF file")
    encrypt_parser.add_argument('output_pdf', help="Output PDF file")
    encrypt_parser.add_argument('password', help="Password to encrypt the PDF file")

    # Extract Images
    extract_images_parser = subparsers.add_parser('-x', '--extract-images', help="Extract images from a PDF file")
    extract_images_parser.add_argument('input_pdf', help="Input PDF file")
    extract_images_parser.add_argument('output_dir', help="Output directory for images")

    # Images to PDF
    images_to_pdf_parser = subparsers.add_parser('-i', '--images-to-pdf', help="Convert images to a PDF file")
    images_to_pdf_parser.add_argument('image_files', nargs='+', help="Input image files")
    images_to_pdf_parser.add_argument('output_pdf', help="Output PDF file")

    args = parser.parse_args()

    if args.command == 'merge':
        merge_pdfs(args.input_pdfs, args.output_pdf)
    elif args.command == 'split':
        split_pdfs(args.input_pdf, args.output_dir, args.split_type, args.i)
    elif args.command == 'extract-text':
        extract_text(args.input_pdf, args.output_txt)
    elif args.command == 'rotate':
        rotate_pages(args.input_pdf, args.output_pdf, args.rotation, args.pages)
    elif args.command == 'watermark':
        add_watermark(args.input_pdf, args.output_pdf, args.watermark_pdf)
    elif args.command == 'encrypt':
        encrypt_pdf(args.input_pdf, args.output_pdf, args.password)
    elif args.command == 'extract-images':
        extract_images(args.input_pdf, args.output_dir)
    elif args.command == 'images-to-pdf':
        images_to_pdf(args.image_files, args.output_pdf)

if __name__ == "__main__":
    main()
