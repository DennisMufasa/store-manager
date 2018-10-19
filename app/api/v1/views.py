"""API endpoints"""
# third-party imports
from flask import jsonify, request, make_response, session, url_for, redirect
from . import v1_bp
# local imports
from .models import *
# routes
@v1_bp.route('/products', methods=['GET', 'POST'])
def get_products():
    """get all products and add a new product"""
    if not session.get("logged_in"):
        return redirect(url_for('login'), code=302)
    if request.method == 'POST':
        request_data = request.get_json()
        if not request_data:
            return make_response(jsonify({"Message":"Enter Product Details!"}))
        sale = Sale(request_data["name"],
        request_data["category"],
        request_data["quantity"],
        request_data["unit_cost"])
        return make_response(jsonify({"Message": sale.add_product()}))
    return make_response(jsonify({"Message": sale.get_products()}))
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