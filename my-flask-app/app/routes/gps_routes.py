from flask import Blueprint, jsonify, request
from app.services.gps_service import get_location_data, update_location_data

gps_bp = Blueprint('gps', __name__)

@gps_bp.route('/location', methods=['GET'])
def get_location():
    location_data = get_location_data()
    return jsonify(location_data), 200

@gps_bp.route('/location', methods=['POST'])
def update_location():
    data = request.json
    updated_data = update_location_data(data)
    return jsonify(updated_data), 200