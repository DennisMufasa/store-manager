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
    def __init__(self, email, username, password, role):
        """class constructor"""
        self.email = email
        self.username = username
        self.password = password
        self.role = role
    def valiadte_credentials(self):
        if  bool(re.search(r'@', self.email)) is False:
            return "Your email should have an @ somewhere!"
        for user in USERS:
            if user["email"] == self.email:
                return "That email is already registered!"
        if self.role != "admin" and self.role != "attendant":
            return "Roles are that of the admin and attendant only!"
        return True
    def add_user(self):
        """Create a new user"""
        # global variable
        global user_id
        if self.valiadte_credentials() is True:
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
        for user in USERS:
            if user['username'] == credentials["username"] and user['password'] == credentials["password"]:
                return "Validation Successful!"
        return "Invalid credentials"


class Product:
    """A class to represent inventory"""
    def __init__(self, name, category, qty, unit_cost):
        """class constructor"""
        self.name = name
        self.category = category
        self.qty = qty
        self.unit_cost = unit_cost
        self.total_cost = self.qty * self.unit_cost
    def validate_products(self):
        """Check validity of product details"""
        if self.qty < 5:
            return "Store requires at least five products of every type!"
        if self.category not in CATEGORY:
            return "Store doesn't sell that category of items!"
        return True
    def add_product(self):
        """Add a new product"""
        if self.validate_products() is True:
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
                return "No products with that is exist!"
            return product
    def edit_category(self, productId, category):
        """Change product category"""
        if isinstance(productId, int) is False:
            return "Product id should be a number!"
        if isinstance(category, str) is False:
            return "Category should be a word!"
        if category not in CATEGORY:
            return "Items of that category are not present in store!"
        for product in INVENTORY:
            if productId not in product:
                return "That product doesn't exist in Inventory!"
            else:
                product["product_category"] = category
                return "Category changed to ", category
    def edit_cost(self, productId, cost):
        """Change product cost"""
        if isinstance(productId, int) is False:
            return "Product id should be a number"
        if isinstance(cost, int) is False:
            return "Currencies should be numbers!"
        for product in INVENTORY:
            if productId not in product:
                return "That product doesn't exist in Inventory!"
            else:
                product["product_unit_cost"] = cost
                return "Unit cost changed to ", cost


class Sale(Product):
    """A class representing a sale.
    This class inherits from Product class"""
    def __init__(self, name, category, qty, unit_cost):
        """class constructor"""
        Product.__init__(self, name, category, qty, unit_cost)
    def create_sale(self, username, product_name, quantity):
        """creating a new sale"""
        #global variable
        global sale_id
        if not INVENTORY:
            return "There are no products in inventory!"
        if isinstance(quantity, int) is False:
            return "Are you serious, quantity should be a number!"
        for product in INVENTORY:
            if product_name not in product.values():
                return "That item is not sold in this store!"
            else:
                tosell = product
                if tosell["product_quantity"] - quantity <= 4:
                    return "That product is currently out of stock!"
                else:
                    bill = tosell["unit_cost"] * quantity
                    date = datetime.datetime.now()
                    formatted_date = date.strftime("%c")
                    SALES.append({
                        "sale_id": sale_id,
                        "attendant": username,
                        "product": product,
                        "quantity": quantity,
                        "Bill": bill,
                        "Date": formatted_date
                    })
                    sale_id += 1
                    tosell["product_quantity"] = tosell["product_qauntity"] - quantity
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
