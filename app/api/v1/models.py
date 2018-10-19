"""Write model classes to be consumed by the APIs"""
# third-party imports
import re
import datetime
# global variables
USERS = []
user_id = 1
INVENTORY = []
CATEGORY = ["furniture", "electronics", "sports", "accessories"]
product_id = 1
SALES = []
sale_id = 1
# models
class User:
    """A model to represent a user"""
    def __init__(self):
        """class constructor"""
        self.email = ""
        self.username = ""
        self.password = ""
        self.role = ""
    @staticmethod
    def valiadte_credentials(credentials):
        """Check user crednetials for anomalies before registration"""
        if not credentials:
            return "Enter data for the server to process!"
        if  bool(re.search(r'@', credentials["email"])) is False:
            return "Your email should have an @ somewhere!"
        for user in USERS:
            if user["email"] == credentials["email"]:
                return "That email is already registered!"
        if credentials["role"] != "admin" and credentials["role"] != "attendant":
            return "Roles are that of the admin and attendant only!"
        return True
    def add_user(self, credentials):
        """Create a new user"""
        # global variable
        global user_id
        # check credentials for data
        if not credentials:
            return "Enter some data for the server to process!"
        # check validity of data
        if self.valiadte_credentials(credentials) is True:
            USERS.append({
                "user_id": user_id,
                "email": self.email,
                "username": self.username,
                "password": self.password,
                "role": self.role
            })
            user_id += 1
            return "User added Successfully!"
        else:
            return "Confirm your credentials before adding a user!"
    def get_users(self):
        """get all users"""
        if not USERS:
            return "There are no users registered!"
        return USERS
    def get_one_user(self, userId):
        """fetch a specific user"""
        if isinstance(userId, int) is False:
            return "User_id should be a number!"
        for user in USERS:
            if userId not in user.values():
                return "No user with that is is registered!"
            return user
    def validate_user(self, credentials):
        """validate user credentials during login"""
        if not credentials:
            return "Enter data for the server to process!"
        if not USERS:
            return "No useres registered. Consult admin for assistance!"
        for user in USERS:
            if user['username'] == credentials["username"] and user['password'] == credentials["password"]:
                return "Login Successful!"
        return "Invalid credentials"


class Product:
    """A class to represent inventory"""
    def __init__(self):
        """class constructor"""
        self.name = ""
        self.category = ""
        self.qty = 0
        self.unit_cost = 0
        self.total_cost = self.qty * self.unit_cost
    @staticmethod
    def validate_products(product_details):
        """Check validity of product details"""
        if product_details["quantity"] < 5:
            return "Store requires at least five products of every type!"
        if product_details["category"] not in CATEGORY:
            return "Store doesn't sell that category of items!"
        return True
    def add_product(self, product_details):
        """Add a new product"""
        if self.validate_products(product_details) is True:
            global product_id
            INVENTORY.append({
                "product_id": product_id,
                "product_name": self.name,
                "product_category": self.category,
                "product_quantity": self.qty,
                "product_unit_cost": self.unit_cost,
                "product_total_worth": self.total_cost 
            })
            product_id += 1
            return "New product added!"
        return "Check product details before adding to inventory!"
    def get_products(self):
        if not INVENTORY:
            return "There are no products in inventory!"
        return INVENTORY
    def get_one_product(self, productId):
        """fetch specific product from invenotry"""
        if isinstance(productId, int) is False:
            return "product id should be a number"
        for product in INVENTORY:
            if productId not in product.values():
                return "No products with that id exist!"
            return product
    def edit_category(self, edit):
        """Change product category"""
        if not edit:
            return "Enter product name to edit and category to change to!"
        if edit["category"] not in CATEGORY:
            return "Items of that category are not present in store!"
        for product in INVENTORY:
            if edit["name"] not in product.values():
                return "That product doesn't exist in Inventory!"
            else:
                product["product_category"] = edit["category"]
                return "Category changed to ", edit["category"]
    def edit_cost(self, edit):
        """Change product cost"""
        if not edit:
            return "Enter product name to edit and cost to change to!"
        if isinstance(edit["cost"], int) is False:
            return "Currencies should be numbers!"
        for product in INVENTORY:
            if edit["name"] not in product.values():
                return "That product doesn't exist in Inventory!"
            else:
                product["product_unit_cost"] = edit["cost"]
                return "Unit cost changed to ", edit["cost"]


class Sale(Product):
    """A class representing a sale.
    This class inherits from Product class"""
    def __init__(self):
        """class constructor"""
        Product.__init__(self)
    def create_sale(self, sale_details):
        """creating a new sale"""
        if not sale_details:
            return "Enter sale details to save!"
        #global variable
        global sale_id
        if not INVENTORY:
            return "There are no products in inventory!"
        if isinstance(sale_details["quantity"], int) is False and sale_details["quantity"] == 0:
            return "Make sure quantity is sensible!"
        for product in INVENTORY:
            if sale_details["product_name"] not in product.values():
                return "That item is not sold in this store!"
            else:
                tosell = product
                if tosell["product_quantity"] - sale_details["quantity"] <= 4:
                    return "That product is currently out of stock!"
                else:
                    bill = tosell["unit_cost"] * sale_details["quantity"]
                    date = datetime.datetime.now()
                    formatted_date = date.strftime("%c")
                    SALES.append({
                        "sale_id": sale_id,
                        "attendant": sale_details["username"],
                        "product": sale_details["product_name"],
                        "quantity": sale_details["quantity"],
                        "Bill": bill,
                        "Date": formatted_date
                    })
                    sale_id += 1
                    tosell["product_quantity"] = tosell["product_qauntity"] - sale_details["quantity"]
                    return "New sale record created!"
    def get_sales(self):
        """get all sale records"""
        if not SALES:
            return "No sales records have been created!"
        return SALES
    def get_one_sale(self, sale_id):
        """Fetch a specific sale record"""
        if not SALES:
            return "No sales records have been created!"
        if isinstance(sale_id, int) is False:
            return "Sale_id should be a number!"
        for sale in SALES:
            if sale_id not in sale.values():
                return "That sale doesn't exist!"
            return sale
    def get_attendant_sales(self, attendant):
        """Fetch all sales per attendant"""
        if not SALES:
            return "There are no sales currently!"
        for sale in SALES:
            if attendant not in sale.values():
                continue
            return sale
        
