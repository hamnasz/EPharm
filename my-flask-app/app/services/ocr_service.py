import pytesseract
import cv2

def extract_text_from_image(image_path):
    try:
        # Load image using OpenCV
        image = cv2.imread(image_path)

        # Preprocess for better OCR accuracy
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # OCR with pytesseract
        text = pytesseract.image_to_string(thresh)

        return text.strip()
    except Exception as e:
        print(f"OCR error: {e}")
        return ""
