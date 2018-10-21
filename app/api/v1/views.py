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
@v1_bp.route('/edit/attendant/<user_id>')
def change_attendant_role(user_id):
    """Admin makes an attendant an admin"""
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }))
    return make_response(jsonify({
        "Message": user.edit_user_role(user_id)
    }))