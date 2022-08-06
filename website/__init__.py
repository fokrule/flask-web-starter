from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    """
    Initializes and configures the Flask application instance.
    """
    app = Flask(__name__)

    # Essential for security, especially for session management.
    # Replace 'dsjhnsljskls shs' with a strong, unique key in a real project.
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # Import blueprints to modularize our application.
    # Blueprints help organize routes and views into separate, manageable sections.
    from .views import views
    from .auth import auth

    # Register blueprints with the main application.
    # The url_prefix ensures routes defined in these blueprints are accessible
    # from the base URL (e.g., /login, /home).
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app




