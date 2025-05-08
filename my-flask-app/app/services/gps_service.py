from flask import Blueprint, request, jsonify
from app.models.store import Store
from app.utils.jwt_handler import get_user_from_request
from geopy.distance import geodesic

gps_bp = Blueprint('gps', __name__)

# Find nearby stores based on user coordinates
@gps_bp.route('/nearby', methods=['POST'])
def get_nearby_stores():
    user_id = get_user_from_request()
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    user_lat = data.get("latitude")
    user_lon = data.get("longitude")

    if user_lat is None or user_lon is None:
        return jsonify({"message": "Coordinates required"}), 400

    user_location = (user_lat, user_lon)
    stores = Store.query.all()
    nearby = []

    for store in stores:
        store_location = (store.latitude, store.longitude)
        distance_km = geodesic(user_location, store_location).km
        if distance_km <= 10:  # Example: limit to 10 km
            nearby.append({
                "store": store.serialize(),
                "distance_km": round(distance_km, 2)
            })

    return jsonify(nearby)
