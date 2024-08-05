import unittest
from unittest.mock import patch, MagicMock
from pdf_utils.extract_images import extract_images

class TestExtractImages(unittest.TestCase):

    @patch('pdf_utils.extract_images.PdfReader')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_extract_images(self, mock_open, MockPdfReader):
        mock_reader_instance = MockPdfReader.return_value
        mock_page = MagicMock()
        mock_reader_instance.pages = [mock_page]
        xObject = {
            '/Im0': MagicMock(_data=b'image_data', get_object=MagicMock(return_value={'/Subtype': '/Image'}))
        }
        mock_page.__getitem__.return_value = {'/XObject': xObject}

        input_pdf = 'input.pdf'
        output_dir = 'output_dir'

        extract_images(input_pdf, output_dir)
        mock_open.assert_called_once_with(f'{output_dir}/image_1_Im0.png', 'wb')
        mock_open().write.assert_called_once_with(b'image_data')

if __name__ == '__main__':
    unittest.main()
