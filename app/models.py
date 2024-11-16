from app.database import db

class Flavor(db.Model):
    __tablename__ = 'flavors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    details = db.Column(db.String(255), nullable=True)

class StockItem(db.Model):
    __tablename__ = 'stock_items'
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String(120), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)

class CustomerFeedback(db.Model):
    __tablename__ = 'customer_feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(120), nullable=False)
    suggestion = db.Column(db.String(255), nullable=False)
    allergy_info = db.Column(db.String(255), nullable=True)