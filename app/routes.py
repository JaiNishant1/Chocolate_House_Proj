from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Flavor, StockItem, CustomerFeedback

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/')
def homepage():
    return jsonify({'message': 'Welcome to Chocolate Shop API'})

@routes_blueprint.route('/flavors', methods=['GET', 'POST'])
def manage_flavors():
    if request.method == 'POST':
        flavor_name = request.json.get('flavor_name')
        flavor_details = request.json.get('flavor_details')
        if flavor_name:
            new_flavor = Flavor(name=flavor_name, details=flavor_details)
            db.session.add(new_flavor)
            db.session.commit()
            return jsonify({'message': 'Flavor added successfully!'}), 201
        return jsonify({'error': 'Flavor name is required.'}), 400
    
    all_flavors = Flavor.query.all()
    return jsonify([{'name': f.name, 'details': f.details} for f in all_flavors])

@routes_blueprint.route('/inventory', methods=['GET', 'POST'])
def manage_inventory():
    if request.method == 'POST':
        ingredient_name = request.json.get('ingredient_name')
        ingredient_quantity = request.json.get('ingredient_quantity')
        if ingredient_name and isinstance(ingredient_quantity, int):
            new_item = StockItem(ingredient=ingredient_name, quantity=ingredient_quantity)
            db.session.add(new_item)
            db.session.commit()
            return jsonify({'message': 'Inventory item added!'}), 201
        return jsonify({'error': 'Valid ingredient name and quantity are required.'}), 400

    stock_list = StockItem.query.all()
    return jsonify([{'ingredient': s.ingredient, 'quantity': s.quantity} for s in stock_list])

@routes_blueprint.route('/feedback', methods=['GET', 'POST'])
def customer_feedback():
    if request.method == 'POST':
        customer_name = request.json.get('customer_name')
        suggestion_text = request.json.get('suggestion_text')
        allergy_details = request.json.get('allergy_details')

        if customer_name and suggestion_text:
            feedback_entry = CustomerFeedback(
                customer_name=customer_name,
                suggestion=suggestion_text,
                allergy_info=allergy_details
            )
            db.session.add(feedback_entry)
            db.session.commit()
            return jsonify({'message': 'Feedback submitted!'}), 201
        return jsonify({'error': 'Customer name and suggestion are required.'}), 400

    feedback_list = CustomerFeedback.query.all()
    return jsonify([
        {
            'customer_name': f.customer_name,
            'suggestion': f.suggestion,
            'allergy_info': f.allergy_info
        } for f in feedback_list
    ])