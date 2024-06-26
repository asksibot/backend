#Initialize Flask app and bring together other components

Initializes your Flask app and brings together other components
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuration settings
    app.config.from_pyfile('config.py')
    
    # Initialize routes
    from . import routes
    app.register_blueprint(routes.bp)
    
    # Additional initialization can go here
    
    return app
