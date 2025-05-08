from flask import Blueprint, request, jsonify
from app.models.medicine import Medicine

medicine_bp = Blueprint('medicine', __name__)

@medicine_bp.route('/medicines', methods=['GET'])
def get_medicines():
    medicines = Medicine.query.all()
    return jsonify([medicine.to_dict() for medicine in medicines]), 200

@medicine_bp.route('/medicines', methods=['POST'])
def add_medicine():
    data = request.get_json()
    new_medicine = Medicine(name=data['name'], dosage=data['dosage'])
    new_medicine.save()
    return jsonify(new_medicine.to_dict()), 201

@medicine_bp.route('/medicines/<int:medicine_id>', methods=['PUT'])
def update_medicine(medicine_id):
    data = request.get_json()
    medicine = Medicine.query.get_or_404(medicine_id)
    medicine.name = data['name']
    medicine.dosage = data['dosage']
    medicine.save()
    return jsonify(medicine.to_dict()), 200

@medicine_bp.route('/medicines/<int:medicine_id>', methods=['DELETE'])
def delete_medicine(medicine_id):
    medicine = Medicine.query.get_or_404(medicine_id)
    medicine.delete()
    return jsonify({'message': 'Medicine deleted successfully'}), 204