import unittest
from unittest.mock import patch, MagicMock
from pdf_utils.extract_text import extract_text

class TestExtractText(unittest.TestCase):

    @patch('PyPDF2.PdfReader')
    def test_extract_text(self, MockPdfReader):
        mock_reader_instance = MockPdfReader.return_value
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "Sample text"
        mock_reader_instance.pages = [mock_page]

        input_pdf = 'input.pdf'
        output_txt = 'output.txt'

        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            extract_text(input_pdf, output_txt)
            mock_file.assert_called_once_with(output_txt, 'w')
            mock_file().write.assert_called_once_with("Sample text\n")

if __name__ == '__main__':
    unittest.main()
