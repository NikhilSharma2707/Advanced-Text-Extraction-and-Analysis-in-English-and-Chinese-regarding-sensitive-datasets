import pytesseract
from PIL import Image

def ocr_image(image_path):
    """Extract text from an image using OCR."""
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

# Test the function
if __name__ == "__main__":
    sample_image = "../data/input/sample_image.png"
    extracted_text = ocr_image(sample_image)
    print(extracted_text)
