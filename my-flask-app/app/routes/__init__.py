# app/routes/__init__.py

from flask import Blueprint

# Initialize the routes blueprint
routes_bp = Blueprint('routes', __name__)

# Import all route modules to register their routes
from . import auth_routes
from . import medicine_routes
from . import cart_routes
from . import ocr_routes
from . import gps_routes
from . import chatbot_routes
from . import invoice_routes