from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('app.config.Config')

    # Initialize blueprints (routes)
    from app.routes.auth_routes import auth_bp
    from app.routes.medicine_routes import medicine_bp
    from app.routes.cart_routes import cart_bp
    from app.routes.ocr_routes import ocr_bp
    from app.routes.gps_routes import gps_bp
    from app.routes.chatbot_routes import chatbot_bp
    from app.routes.invoice_routes import invoice_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(medicine_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(ocr_bp)
    app.register_blueprint(gps_bp)
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(invoice_bp)

    return app

app = create_app()