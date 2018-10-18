"""API endpoints"""
# third-party imports
from flask import jsonify, request, make_response, session
from . import v1_bp
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