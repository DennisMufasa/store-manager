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
@v1_bp.route('/login', methods=['POST'])
def login():
    """Login users into their accounts"""
    if not session.get("logged_in"):
        request_data = request.get_json()
        if user.validate_user(request_data) == "Login Successful!":
            session["logged_in"] = True
            session["username"] = request_data["username"]
            return make_response(jsonify({
                "Message": "Login Successfull!"
            }), 200)
        return make_response(jsonify({
            "Message": "Log in failed! Check your credentials!"
        }))
    return make_response(jsonify({
        "Message": "You are already logged in!"
    }))
@v1_bp.route('/signup')
def signup():
    pass