from flask import Blueprint, request, jsonify
from app import db
from app.models.cart import CartItem
from app.models.medicine import Medicine
from app.utils.jwt_handler import get_user_from_request

cart_bp = Blueprint('cart', __name__)

# View cart items
@cart_bp.route('/', methods=['GET'])
def get_cart():
    user_id = get_user_from_request()
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    result = []
    for item in cart_items:
        med = Medicine.query.get(item.medicine_id)
        result.append({
            "cart_item_id": item.id,
            "medicine": med.serialize(),
            "quantity": item.quantity
        })
    return jsonify(result)

# Add item to cart
@cart_bp.route('/add', methods=['POST'])
def add_to_cart():
    user_id = get_user_from_request()
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    medicine_id = data.get('medicine_id')
    quantity = data.get('quantity', 1)

    # Check if item already in cart
    item = CartItem.query.filter_by(user_id=user_id, medicine_id=medicine_id).first()
    if item:
        item.quantity += quantity
    else:
        item = CartItem(user_id=user_id, medicine_id=medicine_id, quantity=quantity)
        db.session.add(item)

    db.session.commit()
    return jsonify({"message": "Item added to cart"})

# Remove item from cart
@cart_bp.route('/remove/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    user_id = get_user_from_request()
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    item = CartItem.query.get(item_id)
    if not item or item.user_id != user_id:
        return jsonify({"message": "Item not found or unauthorized"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item removed from cart"})
