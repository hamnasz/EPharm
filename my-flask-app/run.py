from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        from app.routes import auth_routes, medicine_routes, cart_routes, ocr_routes, gps_routes, chatbot_routes, invoice_routes
        app.register_blueprint(auth_routes.bp)
        app.register_blueprint(medicine_routes.bp)
        app.register_blueprint(cart_routes.bp)
        app.register_blueprint(ocr_routes.bp)
        app.register_blueprint(gps_routes.bp)
        app.register_blueprint(chatbot_routes.bp)
        app.register_blueprint(invoice_routes.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)