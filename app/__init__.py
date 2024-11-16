from flask import Flask
from app.database import setup_database

def initialize_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secure_random_key'

    # Setup SQLite database
    setup_database(app)

    # Register application routes
    with app.app_context():
        from app.routes import routes_blueprint
        app.register_blueprint(routes_blueprint)

    return app