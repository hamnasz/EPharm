from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.jwt_handler import create_jwt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    new_user.save()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        token = create_jwt(user.id)
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid username or password'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Implement logout functionality if needed
    return jsonify({'message': 'User logged out successfully'}), 200