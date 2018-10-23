"""API endpoints"""
# third-party imports
from flask import jsonify, request, make_response, session, redirect, url_for
from . import v1_blueprint
# local imports
from . import models
# create instances of objects
user = models.User()
sale = models.Sale()
# routes
@v1_blueprint.route('/products', methods=['GET', 'POST'])
def get_products():
    """get all products and add a new product if user == attendant"""
    # if not session.get("logged_in"):
    #     return make_response(jsonify({
    #         "Message": "You are not logged in!"
    #     }))
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
@v1_blueprint.route('/products/<int:productId>')
def get_one_product(productId):
    """Fetch a specific product using its id"""
    # if not session.get("logged_in"):
    #     return make_response(jsonify({
    #         "Message": "You are not logged in!"
    #     }))
    return make_response(jsonify({
        "Message": sale.get_one_product(productId)
    }), 200)
@v1_blueprint.route('/sales', methods=['GET', 'POST'])
def get_sales():
    """Fetch all sales else post a new sale record if an attendant"""
    # if not session.get("logged_in"):
    #     return make_response(jsonify({
    #         "Message": "You are not logged in!"
    #     }))
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
@v1_blueprint.route('/sales/<int:saleId>')
def get_one_sale(saleId):
    """Fetch a specif sale record"""
    # if not session.get("logged_in"):
    #     return make_response(jsonify({
    #         "Message": "You are not logged in!"
    #     }))
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": sale.get_attendant_specific_sale(saleId, session["username"])
        }))
    return make_response(jsonify({
        "Message": sale.get_one_sale(saleId)
    }))
@v1_blueprint.route('/login', methods=['POST'])
def login():
    """Login users into their accounts"""
    # if session.get("logged_in") is None:
    request_data = request.get_json()
    if user.validate_user(request_data) == "Log in successful!":
        # session["logged_in"] = True
        session["username"] = request_data["username"]
        return make_response(jsonify({
            "Message":  "Login Successful!"
        }))
    return make_response(jsonify({
        "Message": "Log in failed! Check your credentials!"
    }))
    # return make_response(jsonify({
    #     "Message": "You are already logged in!"
    # }))
@v1_blueprint.route('/signup', methods=['POST'])
def admin_add_user():
    """Admin can add a new attendant"""
    # if not session.get("logged_in"):
    #     return make_response(jsonify({
    #         "Message": "You are not logged in!"
    #     }))
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }))
    request_data = request.get_json()
    return make_response(jsonify({
        "Message": user.add_user(request_data)
    }))
@v1_blueprint.route('/logout')
def logout():
    # if not session.get("logged_in"):
    #     return "You are not logged in!"
    # session["logged_in"] = False
    session["username"] = ""
    return "Logged out Successfully!"
@v1_blueprint.route('/edit/category', methods=['PUT'])
def edit_category():
    """Admin edit a product category"""
    # if not session.get("logged_in"):
    #     return make_response(jsonify({
    #         "Message": "You are not logged in!"
    #     }))
    if session["username"] != "admin":
        return "you are not an admin!"
    request_data = request.get_json()
    return make_response(jsonify({
        "Message": sale.edit_category(request_data)
    }))
@v1_blueprint.route('/edit/cost', methods=['PUT'])
def edit_cost():
    """Admins edit a product's unit cost"""
    # if not session.get("logged_in"):
    #     return make_response(jsonify({
    #         "Message": "You are not logged in!"
    #     }))
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": "you are not an admin"
        }))
    request_data = request.get_json()
    return make_response(jsonify({
        "Message": sale.edit_cost(request_data)
    }))
@v1_blueprint.route('/edit/quantity', methods=['PUT'])
def edit_product_quantity():
    """admin can add a product quantity"""
    # if not session.get("logged_in"):
    #     return make_response(jsonify({
    #         "Message": "You are not logged in!"
    #     }))
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }))
    request_data = request.get_json()
    return make_response(jsonify({
        "Message": sale.edit_quantity(request_data)
    }))
@v1_blueprint.route('/edit/<user_id>', methods=['PUT'])
def edit_user_role(user_id):
    """An admin can make an attendant an admin"""
    # if not session.get("logged_in"):
    #     return make_response(jsonify({
    #         "Message": "You are not logged in!"
    #     }))
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }))
    return make_response(jsonify({
        "Message": user.edit_user_role(user_id)
    }))
