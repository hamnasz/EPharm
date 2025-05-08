def simple_chat_response(message):
    message = message.lower().strip()

    if "fever" in message:
        return "You may take paracetamol or consult a doctor if symptoms persist."
    elif "headache" in message:
        return "For headaches, drink water and consider mild pain relief like ibuprofen."
    elif "covid" in message:
        return "If you suspect COVID-19, isolate and take a PCR or rapid antigen test."
    elif "how to order" in message or "buy" in message:
        return "To order, upload a prescription or add medicines to your cart and proceed to checkout."
    elif "hello" in message or "hi" in message:
        return "Hello! I’m your E-Pharma assistant. Ask me anything about medicines or prescriptions."
    else:
        return "I’m not sure about that. You can ask about symptoms, ordering, or uploading prescriptions."
