# PDF Tool

A command-line tool for manipulating PDF files. This tool supports merging, splitting, extracting text, rotating, adding watermarks, and encrypting PDFs.

This `README.md` provides clear instructions for installation and usage of the PDF tool, ensuring that you can easily understand and leverage the tool's functionalities.

### Summary of Provided Functionalities

1. **Merge PDFs**: Combines multiple PDFs into a single file.
2. **Split PDFs**: Splits a PDF into smaller files based on page count or parts.
3. **Extract Text**: Extracts text from a PDF and saves it to a text file.
4. **Rotate Pages**: Rotates specified pages of a PDF by a given angle.
5. **Add Watermark**: Adds a watermark to each page of a PDF.
6. **Encrypt PDF**: Encrypts a PDF with a password.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/spageektti/pdf_tool.git
    cd pdf_tool
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Merge PDFs

Merge multiple PDF files into a single PDF.

```sh
python pdf_tool.py -m file1.pdf file2.pdf output.pdf
```

- `file1.pdf` and `file2.pdf` are the input PDFs.
- `output.pdf` is the name of the resulting merged PDF.

### Split PDFs

Split a PDF into smaller PDFs based on the specified criteria.

#### Split every `i` pages:

```sh
python pdf_tool.py -s input.pdf output_dir every i
```

- `input.pdf` is the input PDF.
- `output_dir` is the directory where the split PDFs will be saved.
- `every` specifies the split type to split every `i` pages.
- `i` is the number of pages per split.

#### Split into `i` parts:

```sh
python pdf_tool.py -s input.pdf output_dir parts i
```

- `input.pdf` is the input PDF.
- `output_dir` is the directory where the split PDFs will be saved.
- `parts` specifies the split type to split the PDF into `i` parts.
- `i` is the number of parts.

### Extract Text from a PDF

Extract text from a PDF and save it to a text file.

```sh
python pdf_tool.py -e input.pdf output.txt
```

- `input.pdf` is the input PDF.
- `output.txt` is the text file where the extracted text will be saved.

### Rotate Pages in a PDF

Rotate specified pages of a PDF by a given angle.

```sh
python pdf_tool.py -r input.pdf output.pdf rotation pages
```

- `input.pdf` is the input PDF.
- `output.pdf` is the name of the resulting rotated PDF.
- `rotation` is the rotation angle (90, 180, 270).
- `pages` is a comma-separated list of page numbers or `'all'`.

### Add Watermark to a PDF

Add a watermark to each page of the input PDF.

```sh
python pdf_tool.py -w input.pdf output.pdf watermark.pdf
```

- `input.pdf` is the input PDF.
- `output.pdf` is the name of the resulting watermarked PDF.
- `watermark.pdf` is the PDF containing the watermark.

### Encrypt a PDF

Encrypt a PDF with a given password.

```sh
python pdf_tool.py -p input.pdf output.pdf password
```

- `input.pdf` is the input PDF.
- `output.pdf` is the name of the resulting encrypted PDF.
- `password` is the password to encrypt the PDF.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

