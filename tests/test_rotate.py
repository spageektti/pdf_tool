import unittest
from unittest.mock import patch, MagicMock
from pdf_utils.rotate import rotate_pages

class TestRotatePages(unittest.TestCase):

    @patch('PyPDF2.PdfWriter')
    @patch('PyPDF2.PdfReader')
    def test_rotate_pages(self, MockPdfReader, MockPdfWriter):
        mock_reader_instance = MockPdfReader.return_value
        mock_writer_instance = MockPdfWriter.return_value

        mock_page = MagicMock()
        mock_reader_instance.pages = [mock_page]

        input_pdf = 'input.pdf'
        output_pdf = 'output.pdf'
        rotation = 90
        pages = 'all'

        rotate_pages(input_pdf, output_pdf, rotation, pages)

        mock_page.rotate_clockwise.assert_called_once_with(rotation)
        self.assertTrue(MockPdfWriter.called)
        self.assertTrue(MockPdfReader.called)
        mock_writer_instance.write.assert_called_once_with(output_pdf)

if __name__ == '__main__':
    unittest.main()
