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
def products():
    """get all products and add a new product if user == admin"""
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }), 403)
    if request.method == 'POST':
        if session["username"] == "admin":
            request_data = request.get_json()
            if sale.validate_products(request_data) == "Details are ok!":
                sale.add_product(request_data)
                return make_response(jsonify({
                    "Message": "New product added to inventroy!"
                }))
            return make_response(jsonify({
                "Message": sale.validate_products(request_data)
            }), 409)
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }), 403)
    if isinstance(sale.get_products(), str) is True:
        return make_response(jsonify({
            "Message": "There are no products in inventory!"
        }), 404)
    return make_response(jsonify({
        "Message": sale.get_products()
    }), 200)
    # if request.method == 'GET':
    #     if isinstance(sale.get_products(), str):
    #         return make_response(jsonify({
    #             "Message": "No products stored in inventory!"
    #         }), 404)
    #     return make_response(jsonify({
    #         "Message": sale.get_products()
    #     }), 200)
    # if session["username"] != "admin":
    #     return make_response(jsonify({
    #         "Message": "You are not an admin!"
    #     }), 401)
    # request_data = request.get_json()
    # return make_response(jsonify({
    #     "Message": sale.add_product(request_data)
    # }), 201)
@v1_blueprint.route('/products/<int:productId>')
def fetch_one_product(productId):
    """Fetch a specific product using its id"""
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }), 403)
    if isinstance(sale.get_one_product(productId), str):
        return make_response(jsonify({
            "Message": "Product not found"
        }), 404)
    return make_response(jsonify({
        "Message": sale.get_one_product(productId)
    }), 200)
@v1_blueprint.route('/sales', methods=['GET', 'POST'])
def sales():
    """Fetch all sales else post a new sale record if an attendant"""
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }), 403)
    if request.method == 'POST':
        if session["username"] == "admin":
            return make_response(jsonify({
                "Message": "As an admin, we figured you have better thingd to do!"
            }), 403)
        request_data = request.get_json()
        request_data["username"] = session["username"]
        if sale.create_sale(request_data) == "New sale record created!":
            return make_response(jsonify({
                "Message": "New sale successfully created!"
            }), 201)
        if sale.validate_sale(request_data) == "There are no products in inventory!":
            return make_response(jsonify({
                "Message": "There are no products in inventory!"
            }), 404)
        return make_response(jsonify({
            "Message": sale.validate_sale(request_data)
        }), 409)
    if session["username"] == "admin":
        if isinstance(sale.get_sales(), str) is True:
            return make_response(jsonify({
                "Message": "No sales records have been created!"
            }), 404)
        return make_response(jsonify({
            "Message": sale.get_sales()
        }), 200)
    if isinstance(sale.get_attendant_sales(session["username"]), str) is True:
        return make_response(jsonify({
            "Message": "There are no sales currently!"
        }), 404)
    return make_response(jsonify({
        "Message": sale.get_attendant_sales(session["username"])
    }), 200)
    # if session["username"] != "admin" and request.method == 'POST':
    #     request_data = request.get_json()
    #     request_data["username"] = session["username"]
    #     if sale.create_sale(request_data) != "New sale record created!":
    #         return make_response(jsonify({
    #             "Message": "Invalid product details!"
    #         }), 406)
    #     return make_response(jsonify({
    #         "Message": "New sale record created!"
    #     }), 201)
    # elif session["username"] != "admin":
    #     if isinstance(sale.get_attendant_sales(session["username"]), str):
    #         return make_response(jsonify({
    #             "Message": "You don't have any sale records!"
    #         }), 404)
    #     return make_response(jsonify({
    #         "Message": sale.get_attendant_sales(session["username"])
    #     }), 200)
    # elif session["username"] == "admin" and request.method == 'POST':
    #     # if isinstance(sale.get_sales(), str):
    #     #     return make_response(jsonify({
    #     #         "Message": "There are no sale record created!"
    #     #     }), 404)
    #     return make_response(jsonify({
    #         "Message": "As an admin we figured yud have better things to do!"
    #     }), 403)
    # elif session["username"] == "admin":
    #     if isinstance(sale.get_sales(), str):
    #         return make_response(jsonify({
    #             "Message": sale.get_sales()
    #         }), 404)
    #     return make_response(jsonify({
    #         "Message": sale.get_sales()
    #     }), 200)
@v1_blueprint.route('/sales/<int:saleId>')
def get_one_sale(saleId):
    """Fetch a specif sale record"""
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }), 403)
    if session["username"] != "admin":
        if isinstance(
            sale.get_attendant_specific_sale(saleId, session["username"]), str):
            return make_response(jsonify({
                "Message": "No sale records available with that id!"
            }), 404)
        return make_response(jsonify({
            "Message": sale.get_attendant_specific_sale(saleId, session["username"])
        }), 200)
    if isinstance(sale.get_one_sale(saleId), str):
        return make_response(jsonify({
            "Message": "No sale records available with that id!"
        }), 404)
    return make_response(jsonify({
        "Message": sale.get_one_sale(saleId)
    }), 200)
@v1_blueprint.route('/login', methods=['POST'])
def login():
    """Login users into their accounts"""
    if not session.get("logged_in"):
        request_data = request.get_json()
        if user.validate_user(request_data) == "User validated!":
            if user.login(request_data) == "Login Successfull!":
                session["logged_in"] = True
                session["username"] = request_data["username"]                
                return make_response(jsonify({
                    "Message":  "Login Successful!"
            }), 200)
            return make_response(jsonify({
                "Message": "Invalid Credentials!"
            }), 409)
        return make_response(jsonify({
            "Message": user.validate_user(request_data)
        }), 409)
    return make_response(jsonify({
        "Message": "You have to log out first!"
    }), 403)
@v1_blueprint.route('/signup', methods=['POST'])
def admin_add_user():
    """Admin can add a new attendant"""
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }), 403)
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }), 403)
    request_data = request.get_json()
    if user.add_user(request_data) == "User added Successfully!":
        return make_response(jsonify({
            "Message": "New attendant added!"
        }), 201)
    return make_response(jsonify({
        "Message": user.valiadte_credentials(request_data)
    }), 409)
@v1_blueprint.route('/logout')
def logout():
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }), 403)
    session["logged_in"] = False
    session["username"] = None
    return make_response(jsonify({
        "Message": "Logged out Successfully!"
    }), 200)
@v1_blueprint.route('/edit/category', methods=['PUT'])
def edit_category():
    """Admin edit a product category"""
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }))
    if session["username"] != "admin":
        return "you are not an admin!"
    request_data = request.get_json()
    return make_response(jsonify({
        "Message": sale.edit_category(request_data)
    }))
@v1_blueprint.route('/edit/cost', methods=['PUT'])
def edit_cost():
    """Admins edit a product's unit cost"""
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }))
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
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }))
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
    if not session.get("logged_in"):
        return make_response(jsonify({
            "Message": "You are not logged in!"
        }))
    if session["username"] != "admin":
        return make_response(jsonify({
            "Message": "You are not an admin!"
        }))
    return make_response(jsonify({
        "Message": user.edit_user_role(user_id)
    }))
