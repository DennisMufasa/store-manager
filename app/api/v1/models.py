"""Write model classes to be consumed by the APIs"""
# third-party imports
import re
import datetime
# global variables
USERS = [{
                "user_id": 0,
                "email": "admin@email.com",
                "username": "admin",
                "password": "superuser",
                "role": "admin"
            }]
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
        if len(credentials) != 4:
            return "Ensure attendant details include their email, username, password, role"
        if credentials["username"] == "":
            return "Username cannot be empty!"
        if credentials["email"] == "":
            return "Email cannot be empty!"
        if credentials["password"] == "":
            return "Password cannot be empty!"
        if credentials["role"] == "":
            return "Role cannot be empty!"
        if  bool(re.search(r'@', credentials["email"])) is False:
            return "Your email should have an @ somewhere!"
        if credentials["role"]!="admin" and credentials["role"] != "attendant":
            return "Roles are that of the admin and attendant only!"
        if len(credentials["password"]) < 6:
            return "Password too short! make it at least 6 chars log."        
        for user in range(len(USERS)):
            if USERS[user]["email"] == credentials["email"]:
                return "That email is already registered!"
        return "Details are ok!"
    def add_user(self, credentials):
        """Create a new user"""
        # global variable
        global user_id
        # check validity of data
        if self.valiadte_credentials(credentials) == "Details are ok!":
            self.email = credentials["email"]
            self.username = credentials["username"]
            self.password = credentials["password"]
            self.role = credentials["role"]
            USERS.append({
                "user_id": user_id,
                "email": self.email,
                "username": self.username,
                "password": self.password,
                "role": self.role
            })
            user_id += 1
            return "User added Successfully!"
        return self.valiadte_credentials(credentials)
    def get_users(self):
        """get all users"""
        if not USERS:
            return "There are no users registered!"
        return USERS
    def get_one_user(self, userId):
        """fetch a specific user"""
        if isinstance(userId, int) is False:
            return "User_id should be a number!"
        for user in range(len(USERS)):
            if userId == USERS[user]["user_id"]:
                return USERS[user]
        return "That user_id is not registered to any users!"
    @staticmethod
    def validate_user(credentials):
        """validate user credentials before login"""
        if not credentials:
            return "Enter data for the server to process!"
        if not USERS:
            return "No useres registered. Consult admin for assistance!"       
        if credentials["username"] == "":
            return "Username cannot be empty!"
        if credentials["password"] == "":
            return "Password is required for login!"
        if len(credentials) != 2:
            return "Ensure you have entered a username and password!"
        return "User validated!"
    def login(self, credentials):
        """Login users"""
        if self.validate_user(credentials) == "User validated!":
            for user in range(len(USERS)):
                if USERS[user]["username"] == credentials["username"] and USERS[user]["password"] == credentials["password"]:
                    return "Login Successfull!"
        return self.validate_user(credentials)
    def edit_user_role(self, userId):
        """Admin changes attendant role to admin"""
        if not USERS:
            return "No users registered yet!"
        if isinstance(userId, int) is False:
            return "Please see that user ids are numbers!"
        for user in range(len(USERS)):
            if userId == USERS[user]["user_id"]:
                USERS[user]["role"] = "admin"
                return "Attendant was promoted to admin!"
        return "That user_id is not registered to any users!"


class Product:
    """A class to represent inventory"""
    def __init__(self):
        """class constructor"""
        self.name = ""
        self.category = ""
        self.qty = 0
        self.unit_cost = 0
        self.total_cost = 0
    @staticmethod
    def validate_products(product_details):
        """Check validity of product details"""
        if not product_details:
            return "Enter product details to save"
        if len(product_details) !=4:
            return "Ensure attendant details include their email, username, password, role"
        if product_details["quantity"] < 5:
            return "Store requires at least five products of every type!"
        if isinstance(product_details["quantity"], int) is False:
            return "Get serious! Make sure quantity is a numer!"
        if product_details["category"] not in CATEGORY:
            return "Store doesn't sell that category of items!"
        if product_details["product_name"] == "":
            return "Can't enter product without a name!"
        if product_details["product_unit_cost"] == 0:
            return "The product unit cost cannot be 0"
        if product_details["product_unit_cost"] == "":
            return "Product unit cost cannot be empty!"
        if isinstance(product_details["product_unit_cost"], int) is False:
            return "Product unit cost should obviously be a number!"
        return "Details are ok!"
    def add_product(self, product_details):
        """Add a new product"""
        if self.validate_products(product_details) == "Details are ok!":
            global product_id
            self.name = product_details["product_name"]
            self.category = product_details["category"]
            self.qty = product_details["quantity"]
            self.unit_cost = product_details["product_unit_cost"]
            self.total_cost = self.qty * self.unit_cost
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
        # return self.validate_products(product_details)
    def get_products(self):
        """fetch all available products in inventory if any!"""
        if not INVENTORY:
            return "There are no products in inventory!"
        return INVENTORY
    def get_one_product(self, productId):
        """fetch specific product from invenotry"""
        if isinstance(productId, int) is False:
            return "product id should be a number"
        for product in range(len(INVENTORY)):
            if productId == INVENTORY[product]["product_id"]:
                return INVENTORY[product]
        return "That product_id is not registered to any products!"
    def edit_category(self, edit):
        """Change product category"""
        if not edit:
            return "Enter product name to edit and category to change to!"
        if edit["category"] not in CATEGORY:
            return "Items of that category are not present in store!"
        for product in range(len(INVENTORY)):
            if edit["name"] == INVENTORY[product]["product_name"]:
                INVENTORY[product]["product_category"] = edit["category"]
                return "Category changed to ", edit["category"]
        return "That product is not present in Inventory!"
    def edit_cost(self, edit):
        """Change product cost"""
        if not edit:
            return "Enter product name to edit and cost to change to!"
        if isinstance(edit["cost"], int) is False:
            return "Currencies should be numbers!"
        for product in range(len(INVENTORY)):
            if edit["name"] == INVENTORY[product]["product_name"]:
                INVENTORY[product]["product_unit_cost"] = edit["cost"]
                return "Unit cost changed to ", edit["cost"]
        return "That product is not present in Inventory!"
    def edit_quantity(self, edit):
        """Change an product quantity"""
        if not edit:
            return "Enter product name and quantity of items to add!"
        if isinstance(edit["quantity"], int) is False:
            return "Product quantities should be numbers!"
        for product in range(len(INVENTORY)):
            if edit["name"] == INVENTORY[product]["product_name"]:
                INVENTORY[product]["product_unit_cost"] = (
                    INVENTORY[product]["product_unit_cost"] + edit["quantity"]
                )
                return edit["quantity"],"Products added!"
        return "That product is not present in Inventory!"


class Sale(Product):
    """A class representing a sale.
    This class inherits from Product class"""
    def __init__(self):
        """class constructor"""
        Product.__init__(self)
    @staticmethod
    def validate_sale(sale_details):
        """validate sale details before recording them"""
        if not sale_details:
            return "Enter data for the server to process!"
        if len(sale_details) != 3:
            return "Ensure to include product details and quantity!"
        if isinstance(sale_details["product_name"], str) is False:
            return "Products' names are obviously words(strings)"
        if sale_details["product_name"] == "":
            return "Product name cannot be empty!"
        if sale_details["quantity"] == 0:
            return "Quantity cannot be 0!"
        if sale_details["quantity"] == "":
            return "Quantity cannot be empty!"
        if isinstance(sale_details["quantity"], int) is False:
            return "What are you doing! Quantity should be a number!"
        if not INVENTORY:
            return "There are no products in inventory!"
        # for product in range(len(INVENTORY)):
        #     if sale_details["product_name"] != INVENTORY[product]["product_name"]:
        #         return "That product is not sold here!"
        #     if INVENTORY[product]["product_quantity"] - sale_details["quantity"] <= 4:
        #         return "That product is currently out of stock!"
        return "Sale detail are ok!"
    def create_sale(self, sale_details):
        """creating a new sale"""
        if self.validate_sale(sale_details) == "Sale detail are ok!":
            for product in range(len(INVENTORY)):
                if sale_details["product_name"] == INVENTORY[product]["product_name"]:
                    #global variable
                    global sale_id
                    bill = INVENTORY[product]["product_unit_cost"] * sale_details["quantity"]
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
                    INVENTORY[product]["product_quantity"] = (
                        INVENTORY[product]["product_quantity"] - sale_details["quantity"]
                    )
                    INVENTORY[product]["product_total_worth"] = (
                        INVENTORY[product]["product_quantity"] * INVENTORY[product]["product_unit_cost"]
                    )
            return "New sale record created!"
        return self.validate_sale(sale_details)
    def get_sales(self):
        """get all sale records"""
        if not SALES:
            return "No sales records have been created!"
        return SALES
    def get_one_sale(self, saleId):
        """Fetch a specific sale record"""
        if not SALES:
            return "No sales records have been created!"
        if isinstance(saleId, int) is False:
            return "Sale_id should be a number!"
        for sale in range(len(SALES)):
            if saleId == SALES[sale]["sale_id"]:
                return SALES[sale]
        return "That sale_id is not registered to any sale record!"
    def get_attendant_sales(self, attendant):
        """Fetch all sales per attendant"""
        if not SALES:
            return "There are no sales currently!"
        attendant_sales = []
        for sale in range(len(SALES)):
            if attendant == SALES[sale]["attendant"]:
                attendant_sales.append(SALES[sale])
        return attendant_sales
    def get_attendant_specific_sale(self, my_sale_id, name):
        """Fetch specific sale report for specific attendant"""
        if not SALES:
            return "There are no sale records saved yet?!"
        attendant_sales = self.get_attendant_sales(name)
        for i in range(len(attendant_sales)):
            if my_sale_id == attendant_sales[i]["sale_id"]:
                return attendant_sales[i]
        return "You don't have any sales with that id!"
