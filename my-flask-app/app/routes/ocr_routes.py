from flask import Blueprint, request, jsonify
from app.services.ocr_service import process_image

ocr_routes = Blueprint('ocr_routes', __name__)

@ocr_routes.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        result = process_image(file)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500