"""API endpoints"""
# third-party imports
from flask import jsonify, request, make_response, session, url_for, redirect
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
    pass
@v1_bp.route('/sales/<saleId>')
def get_one_sale(saleId):
    pass
@v1_bp.route('/login', methods=['GET', 'POST'])
def login():
    pass
@v1_bp.route('/signup')
def signup():
    pass