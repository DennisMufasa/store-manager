"""Models that views consume to manipulate data"""
# third-party imports
import re
# local import
from . utils import Database
database = Database()
class User:
    def __init__(self):
        """Class constructor"""
        self.username = ""
        self.password = ""
        self.email = ""
        self.role = ""
    def valiadte_credentials(self, credentials):
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
        return "Details are ok!"
    def add_attendant(self, credentials):
        """Adding a new attendant"""
        if self.valiadte_credentials(credentials) == "Details are ok!":
            username = credentials["username"]
            password = credentials["password"]
            email = credentials["email"]
            role = credentials["role"]
            return database.add_user(username, password, email, role)