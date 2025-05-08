from flask import Blueprint, jsonify, request

invoice_bp = Blueprint('invoice', __name__)

@invoice_bp.route('/invoices', methods=['GET'])
def get_invoices():
    # Logic to retrieve invoices
    return jsonify({"message": "List of invoices"}), 200

@invoice_bp.route('/invoices/<int:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    # Logic to retrieve a specific invoice by ID
    return jsonify({"message": f"Invoice {invoice_id} details"}), 200

@invoice_bp.route('/invoices', methods=['POST'])
def create_invoice():
    # Logic to create a new invoice
    data = request.json
    return jsonify({"message": "Invoice created", "data": data}), 201

@invoice_bp.route('/invoices/<int:invoice_id>', methods=['PUT'])
def update_invoice(invoice_id):
    # Logic to update an existing invoice
    data = request.json
    return jsonify({"message": f"Invoice {invoice_id} updated", "data": data}), 200

@invoice_bp.route('/invoices/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    # Logic to delete an invoice
    return jsonify({"message": f"Invoice {invoice_id} deleted"}), 204