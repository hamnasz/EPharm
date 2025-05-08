from flask import Blueprint, request, jsonify
from app.models.cart import Cart
from app import db

cart_routes = Blueprint('cart_routes', __name__)

@cart_routes.route('/cart', methods=['GET'])
def get_cart():
    user_id = request.args.get('user_id')
    cart = Cart.query.filter_by(user_id=user_id).first()
    if cart:
        return jsonify(cart.to_dict()), 200
    return jsonify({'message': 'Cart not found'}), 404

@cart_routes.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    item_id = data.get('item_id')
    # Logic to add item to cart
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        db.session.add(cart)
    cart.add_item(item_id)
    db.session.commit()
    return jsonify({'message': 'Item added to cart'}), 201

@cart_routes.route('/cart', methods=['DELETE'])
def remove_from_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    item_id = data.get('item_id')
    cart = Cart.query.filter_by(user_id=user_id).first()
    if cart:
        cart.remove_item(item_id)
        db.session.commit()
        return jsonify({'message': 'Item removed from cart'}), 200
    return jsonify({'message': 'Cart not found'}), 404