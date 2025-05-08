from flask import Blueprint, request, jsonify
from app import db
from app.models.medicine import Medicine

medicine_bp = Blueprint('medicine', __name__)

# Get all medicines
@medicine_bp.route('/', methods=['GET'])
def get_all_medicines():
    medicines = Medicine.query.all()
    return jsonify([med.serialize() for med in medicines])

# Get medicine by ID
@medicine_bp.route('/<int:medicine_id>', methods=['GET'])
def get_medicine(medicine_id):
    medicine = Medicine.query.get_or_404(medicine_id)
    return jsonify(medicine.serialize())

# Add a new medicine (admin access in future)
@medicine_bp.route('/', methods=['POST'])
def add_medicine():
    data = request.get_json()
    name = data.get('name')
    manufacturer = data.get('manufacturer')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')

    medicine = Medicine(
        name=name,
        manufacturer=manufacturer,
        description=description,
        price=price,
        stock=stock
    )

    db.session.add(medicine)
    db.session.commit()
    return jsonify({"message": "Medicine added successfully", "medicine": medicine.serialize()}), 201
