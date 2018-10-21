"""API endpoints"""
# third-party imports
from flask import jsonify, request, make_response, session, redirect, url_for
from . import v1_bp
# local imports
from . import models
# create instances of objects
user = models.User()
sale = models.Sale()
# routes
@v1_bp.route('/products', methods=['GET', 'POST'])
def get_products():
    """get all products and add a new product"""
    if not session.get("logged_in"):
        return redirect(url_for('login'), code=302)
    if request.method == 'GET':
        return make_response(jsonify({
            "Message": sale.get_products()
        }))
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }))
    request_data = request.get_json()
    return make_response(jsonify({
        "Message": sale.add_product(request_data)
    }))
@v1_bp.route('/products/<productId>')
def get_one_product(productId):
    pass
@v1_bp.route('/sales', methods=['GET', 'POST'])
def get_sales():
    """Fetch all sales else post a new sale record if an attendant"""
    if not session.get("logged_in"):
        return redirect(url_for('/login'), code=302)
    if session["username"] != "admin" and request.method == 'POST':
        request_data = request.get_json()
        request_data["username"] = session["username"]
        return make_response(jsonify({
            "Message": sale.create_sale(request_data)
        }))
    elif session["username"] != "admin":
        return make_response(jsonify({
            "Message": sale.get_attendant_sales(session["username"])
        }))
    elif session["username"] == "admin":
        return make_response(jsonify({
            "Message": sale.get_sales()
        }))
@v1_bp.route('/sales/<saleId>')
def get_one_sale(saleId):
    pass
@v1_bp.route('/login', methods=['GET', 'POST'])
def login():
    pass
@v1_bp.route('/signup', methods=['POST'])
def signup():
    """Admin can add a new attendant"""
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }))
    request_data = request.get_json()
    return make_response(jsonify({
        "Message": user.add_user(request_data)
    }))
