import os
from flask import Blueprint, jsonify, send_file
from app.models.cart import CartItem
from app.models.medicine import Medicine
from app.utils.jwt_handler import get_user_from_request
from app.utils.invoice_generator import generate_invoice_pdf
from app import db

invoice_bp = Blueprint('invoice', __name__)
INVOICE_FOLDER = 'invoices'
os.makedirs(INVOICE_FOLDER, exist_ok=True)

@invoice_bp.route('/generate', methods=['GET'])
def generate_invoice():
    user_id = get_user_from_request()
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    if not cart_items:
        return jsonify({"message": "Cart is empty"}), 400

    # Prepare data
    items = []
    total = 0
    for item in cart_items:
        med = Medicine.query.get(item.medicine_id)
        cost = med.price * item.quantity
        total += cost
        items.append({
            "name": med.name,
            "price": med.price,
            "quantity": item.quantity,
            "subtotal": cost
        })

    # Generate and return PDF
    invoice_path = generate_invoice_pdf(user_id, items, total)
    return send_file(invoice_path, as_attachment=True)
