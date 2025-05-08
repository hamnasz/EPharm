from flask import current_app
import pytesseract
from PIL import Image
import os

def perform_ocr(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image at {image_path} does not exist.")
    
    # Load the image from the specified path
    image = Image.open(image_path)
    
    # Use pytesseract to perform OCR on the image
    text = pytesseract.image_to_string(image)
    
    return text

def save_uploaded_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return file_path
    else:
        raise ValueError("Invalid file type. Only images are allowed.")

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions