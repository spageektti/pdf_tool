import unittest
from unittest.mock import patch, MagicMock
from pdf_utils.merge import merge_pdfs

class TestMergePDFs(unittest.TestCase):
    
    @patch('PyPDF2.PdfWriter')
    @patch('PyPDF2.PdfReader')
    def test_merge_pdfs(self, MockPdfReader, MockPdfWriter):
        # Mock the PdfReader and PdfWriter
        mock_reader_instance = MockPdfReader.return_value
        mock_writer_instance = MockPdfWriter.return_value

        mock_reader_instance.pages = [MagicMock(), MagicMock()]

        input_pdfs = ['file1.pdf', 'file2.pdf']
        output_pdf = 'output.pdf'

        merge_pdfs(input_pdfs, output_pdf)

        self.assertTrue(MockPdfWriter.called)
        self.assertTrue(MockPdfReader.called)
        self.assertEqual(MockPdfReader.call_count, len(input_pdfs))
        self.assertEqual(mock_writer_instance.add_page.call_count, 2)
        mock_writer_instance.write.assert_called_once_with(output_pdf)

if __name__ == '__main__':
    unittest.main()
