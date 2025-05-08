from flask import Blueprint, request, jsonify

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chatbot/message', methods=['POST'])
def handle_message():
    data = request.json
    user_message = data.get('message')
    
    # Here you would typically process the message and generate a response
    # For now, we'll just echo the message back
    response_message = f"You said: {user_message}"
    
    return jsonify({"response": response_message})

@chatbot_bp.route('/chatbot/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})