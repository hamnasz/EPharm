import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app import db
from app.models.prescription import Prescription
from app.utils.jwt_handler import get_user_from_request
from app.services.ocr_service import extract_text_from_image

ocr_bp = Blueprint('ocr', __name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Upload image and perform OCR
@ocr_bp.route('/upload', methods=['POST'])
def upload_prescription():
    user_id = get_user_from_request()
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    if 'image' not in request.files:
        return jsonify({"message": "No image part"}), 400

    file = request.files['image']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({"message": "Invalid file type"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # OCR processing
    extracted_text = extract_text_from_image(filepath)

    # Save to DB
    prescription = Prescription(
        user_id=user_id,
        image_path=filepath,
        extracted_text=extracted_text
    )
    db.session.add(prescription)
    db.session.commit()

    return jsonify({
        "message": "Prescription uploaded and processed",
        "text": extracted_text,
        "prescription_id": prescription.id
    }), 201
