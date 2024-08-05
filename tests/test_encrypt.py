import unittest
from unittest.mock import patch, MagicMock
from pdf_utils.encrypt import encrypt_pdf

class TestEncryptPDF(unittest.TestCase):

    @patch('PyPDF2.PdfWriter')
    @patch('PyPDF2.PdfReader')
    def test_encrypt_pdf(self, MockPdfReader, MockPdfWriter):
        mock_reader_instance = MockPdfReader.return_value
        mock_writer_instance = MockPdfWriter.return_value

        mock_reader_instance.pages = [MagicMock(), MagicMock()]

        input_pdf = 'input.pdf'
        output_pdf = 'output.pdf'
        password = 'password'

        encrypt_pdf(input_pdf, output_pdf, password)

        self.assertTrue(MockPdfWriter.called)
        self.assertTrue(MockPdfReader.called)
        self.assertEqual(mock_writer_instance.add_page.call_count, 2)
        mock_writer_instance.encrypt.assert_called_once_with(password)
        mock_writer_instance.write.assert_called_once_with(output_pdf)

if __name__ == '__main__':
    unittest.main()
