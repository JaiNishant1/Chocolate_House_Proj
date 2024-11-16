from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chocolate_shop.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Initialize database models
    with app.app_context():
        from app.models import Flavor, StockItem, CustomerFeedback
        db.create_all()