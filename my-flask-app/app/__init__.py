from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('app.config.Config')

    db.init_app(app)

    # Import blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.medicine_routes import medicine_bp
    # Add other routes here as needed

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(medicine_bp, url_prefix='/api/medicines')

    return app
