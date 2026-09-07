import fitz
import pytesseract
from PIL import Image
import io


def extract_pdf_content(pdf_path):

    document = fitz.open(pdf_path)

    full_text = ""
    photo_present = False

    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    for page_number, page in enumerate(document):

        images = page.get_images(full=True)

        if len(images) > 0:
            photo_present = True

        print(f"\n--- Page {page_number + 1} ---")

        text = page.get_text()

        print("Text length:", len(text))

        if text.strip():

            print("Text found")

            full_text += text + "\n"

        else:

            print("No text found - OCR may be required")
            print("Running OCR...")

            pix = page.get_pixmap()

            img = Image.open(
                io.BytesIO(
                    pix.tobytes("png")
                )
            )

            ocr_text = pytesseract.image_to_string(img)

            print("OCR text length:", len(ocr_text))

            full_text += ocr_text + "\n"

    document.close()

    return full_text, photo_present