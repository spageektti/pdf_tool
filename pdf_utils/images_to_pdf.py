from PIL import Image

def images_to_pdf(image_files, output_pdf):
    images = [Image.open(image).convert('RGB') for image in image_files]
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
