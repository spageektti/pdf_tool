import unittest
from unittest.mock import patch, MagicMock
from pdf_utils.split import split_pdfs

class TestSplitPDFs(unittest.TestCase):

    @patch('PyPDF2.PdfWriter')
    @patch('PyPDF2.PdfReader')
    def test_split_pdfs_every(self, MockPdfReader, MockPdfWriter):
        mock_reader_instance = MockPdfReader.return_value
        mock_writer_instance = MockPdfWriter.return_value

        mock_reader_instance.pages = [MagicMock() for _ in range(10)]

        input_pdf = 'input.pdf'
        output_dir = 'output_dir'
        split_type = 'every'
        i = 2

        split_pdfs(input_pdf, output_dir, split_type, i)

        self.assertTrue(MockPdfWriter.called)
        self.assertTrue(MockPdfReader.called)
        self.assertEqual(MockPdfWriter.call_count, 5)  # 10 pages / 2 per split

    @patch('PyPDF2.PdfWriter')
    @patch('PyPDF2.PdfReader')
    def test_split_pdfs_parts(self, MockPdfReader, MockPdfWriter):
        mock_reader_instance = MockPdfReader.return_value
        mock_writer_instance = MockPdfWriter.return_value

        mock_reader_instance.pages = [MagicMock() for _ in range(10)]

        input_pdf = 'input.pdf'
        output_dir = 'output_dir'
        split_type = 'parts'
        i = 2

        split_pdfs(input_pdf, output_dir, split_type, i)

        self.assertTrue(MockPdfWriter.called)
        self.assertTrue(MockPdfReader.called)
        self.assertEqual(MockPdfWriter.call_count, 2)  # 2 parts

if __name__ == '__main__':
    unittest.main()
