import unittest
from unittest.mock import patch, MagicMock
from pdf_utils.watermark import add_watermark

class TestAddWatermark(unittest.TestCase):

    @patch('PyPDF2.PdfWriter')
    @patch('PyPDF2.PdfReader')
    def test_add_watermark(self, MockPdfReader, MockPdfWriter):
        mock_reader_instance = MockPdfReader.return_value
        mock_writer_instance = MockPdfWriter.return_value

        mock_reader_instance.pages = [MagicMock(), MagicMock()]
        mock_watermark_page = MagicMock()
        mock_watermark_reader = MagicMock()
        mock_watermark_reader.pages = [mock_watermark_page]

        with patch('pdf_utils.watermark.PyPDF2.PdfReader', return_value=mock_watermark_reader):
            input_pdf = 'input.pdf'
            output_pdf = 'output.pdf'
            watermark_pdf = 'watermark.pdf'

            add_watermark(input_pdf, output_pdf, watermark_pdf)

            for page in mock_reader_instance.pages:
                page.merge_page.assert_called_once_with(mock_watermark_page)
            self.assertTrue(MockPdfWriter.called)
            self.assertTrue(MockPdfReader.called)
            mock_writer_instance.write.assert_called_once_with(output_pdf)

if __name__ == '__main__':
    unittest.main()
