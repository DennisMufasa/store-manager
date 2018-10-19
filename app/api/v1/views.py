"""API endpoints"""
# third-party imports
from flask import jsonify, request, make_response, session
from . import v1_bp
# local imports
from . import models
# create instances of objects
user = models.User()
sale = models.Sale()
# routes
@v1_bp.route('/products', methods=['GET', 'POST'])
def get_products():
    pass
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
@v1_bp.route('/logout')
def logout():
    if not session.get("logged_in"):
        return "You are not logged in!"
    session["logged_in"] = False
    session["username"] = ""
    return "Logged out Successfully!"