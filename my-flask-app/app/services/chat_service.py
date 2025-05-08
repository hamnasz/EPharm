from flask import jsonify

def get_chatbot_response(user_input):
    # Placeholder function to simulate chatbot response
    # In a real application, this would interface with a chatbot API or model
    response = f"Chatbot response to: {user_input}"
    return response

def handle_chat_request(user_input):
    response = get_chatbot_response(user_input)
    return jsonify({"response": response})