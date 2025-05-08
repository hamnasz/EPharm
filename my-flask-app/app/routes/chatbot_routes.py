from flask import Blueprint, request, jsonify
from app.utils.jwt_handler import get_user_from_request
from app.services.chat_service import simple_chat_response

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/', methods=['POST'])
def chat():
    user_id = get_user_from_request()
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    message = data.get('message', '')

    if not message:
        return jsonify({"message": "Empty input"}), 400

    response = simple_chat_response(message)
    return jsonify({"response": response})
