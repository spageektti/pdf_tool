import unittest
from unittest.mock import patch, MagicMock
from pdf_utils.images_to_pdf import images_to_pdf

class TestImagesToPDF(unittest.TestCase):

    @patch('pdf_utils.images_to_pdf.Image.open')
    def test_images_to_pdf(self, mock_open):
        mock_image_instance = MagicMock()
        mock_open.return_value = mock_image_instance
        mock_image_instance.convert.return_value = mock_image_instance

        image_files = ['image1.png', 'image2.png']
        output_pdf = 'output.pdf'

        images_to_pdf(image_files, output_pdf)
        mock_open.assert_any_call('image1.png')
        mock_open.assert_any_call('image2.png')
        mock_image_instance.convert.assert_called_with('RGB')
        mock_image_instance.save.assert_called_once_with(output_pdf, save_all=True, append_images=[mock_image_instance, mock_image_instance])

if __name__ == '__main__':
    unittest.main()
