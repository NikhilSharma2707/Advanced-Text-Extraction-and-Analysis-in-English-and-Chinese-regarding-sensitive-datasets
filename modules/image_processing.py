import PyPDF2
from PIL import Image
import io

def extract_images_from_pdf(pdf_path):
    """Extract images from a PDF file."""
    images = []
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            if '/XObject' in page['/Resources']:
                xObject = page['/Resources']['/XObject'].get_object()
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        img = xObject[obj]
                        img_data = img._data
                        image = Image.open(io.BytesIO(img_data))
                        images.append(image)
    return images

# Test the function
if __name__ == "__main__":
    sample_pdf = "../data/input/sample.pdf"
    images = extract_images_from_pdf(sample_pdf)
    for i, img in enumerate(images):
        img.save(f"../data/output/image_{i}.png")
