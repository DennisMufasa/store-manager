# """Tests for vesrion 1 of store-manager APIs"""
# # third-party import
import pytest
import unittest
import json
# local import
from app.api import create_app
class Base_Test_class(unittest.TestCase):
    """Class holding configurations for testing"""
    def create_app(self):
        """create app to test"""
        app = create_app('testing')
        return app
    def setup(self):
        """set up an instance of the app for testing"""
        self.app = self.create_app()
        self.app.testing = True
        self.context = self.app.app_context()
        self.context.push()
    def tear_down(self):
        """Clean up after testing"""
        self.context.pop()


class Test_product_views(Base_Test_class):
    """Tests endpoints that handle products"""
    # def __init__(self):
    #     """Constructor for test_product_views"""
    #     Base_Test_class.__init__(self)
    def test_products(self):
        """test get all products endpoint when not logged in"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                response = client.get('/api/v1/products')
                self.assertIsNone(session.get("logged_in"))
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "You are not logged in!")
    def test_products_logged_in(self):
        """test fetch products when no products saved in inventory"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session["logged_in"] = True
                response = client.get('/api/v1/products')
                self.assertTrue(session.get("logged_in"))
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "There are no products in inventory!")
    def test_add_product(self):
        """test add a new product enpoint for a logged in admin"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session["logged_in"] = True
                session["username"] = "admin"
                response = client.post('/api/v1/products', data={
                    "product_name": "playstation 4",
                    "category" : "electronics",
                    "quantity": 10,
                    "product_unit_cost": 40000
                    })
                self.assertTrue(session.get("logged_in"))
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "New product added!")
    def test_attendant_add_product(self):
        """test add a new product enpoint for an attendant"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session["logged_in"] = True
                session["username"] = "attendant"
                response = client.post('/api/v1/products', data={
                    "product_name": "playstation 4",
                    "category" : "electronics",
                    "quantity": 10,
                    "product_unit_cost": 40000
                    })                
                self.assertTrue(session.get("logged_in"))
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "You are not an admin!")                
    def test_get_one_product(self):
        """test get one client endpoint while not logged in"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                response = client.get('/api/v1/products/5')
                self.assertIsNone(session.get("logged_in"))
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "You are not logged in!")
    def test_get_one_product_loggedIn(self):
        """test fetch specific sale when logged in"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session["logged_in"] = True
                response = client.get('/api/v1/product/1')
                self.assertTrue(session.get("logged_in"))
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "That product_id is not registered to any products!")


class Test_Sales_views(Base_Test_class):
    """Tests for sales endpoints"""
    # def __init__(self):
    #     """Test_sales_class consturctor"""
    #     Base_Test_class.__init__(self)
    def test_get_sales(self):
        """test get all sales endpoint when not logged in"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                response = client.get('/api/v1/sales')
                self.assertIsNone(session.get("logged_in"))
                self.assertTrue(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertTrue(response.json["Message"], "You are not logged in!")
    def test_get_sales_loggedin_admin(self):
        """fetch all sales records for users if logged in as admin"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session["logged_in"] = True
                session["username"] = "admin"
                response = client.get('/api/v1/sales')
                self.assertTrue(session.get("logged_in"))
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertTrue(response.json["Message"], "No sales records have been created!")
    def test_get_one_sale(self):
        """Test get one sale endpoint if logged in as attendant"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session["logged_in"] = True
                session["username"] = "attendant"
                response = client.get('/api/v1/sales/1')
                self.assertIsNone(session.get("logged_in"))
                self.assertTrue(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "There are no sale records saved yet?!")
    def test_add_sale(self):
        """Test make sale report endpoint before logging in for attendant"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                response = client.post('/api/v1/sales', data={
                    "attendant": "mufasa",
                    "product": "Playstation 4",
                    "quantity": 2,
                })
                self.assertIsNone(session.get("logged_in"))
                self.assertEqual(response.status_code ,200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "You are not logged in!")
    def test_add_sale_loggedIn(self):
        """Test make sale report endpoint after logging as an attendant"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session["logged_in"] = True
                session["username"] = "wewe"
                response = client.post('/api/v1/sales', data={
                    "attendant": "mufasa",
                    "product": "Playstation 4",
                    "quantity": 2,
                })
                self.assertIsNone(session.get("logged_in"))
                self.assertEqual(response.status_code ,200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "There are no products in inventory!")                
    def test_login(self):
        """test login endpoint"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                response = client.post('/api/v1/login', data={
                    "username": "admin",
                    "password": "superuser"
                })
                self.assertTrue(session.get("logged_in"))
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "Loggin Successful!")
    def test_signup(self):
        """test signup endpoint adds users to the app"""
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session["logged_in"] = True
                session["username"] = "admin"
                response = client.post('/api/v1/signup', data={
                    "email": "mufasa@email.com",
                    "username": "mufasa",
                    "password": "mufasa",
                    "role": "attendant"})
                self.assertTrue(session.get("logged_in"))
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json, dict)
                self.assertEqual(response.json["Message"], "You are not logged in!")
