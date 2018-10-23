"""Tests for vesrion 1 of my APIs"""
# third-party import
import pytest
import json
from flask import session
class Test_view:
    """Tests endpoints"""
    def test_get_products(self, client):
        """test get all products endpoint"""
        response = client.get('/api/v1/products')
        # assert session.get("logged_in") == None
        assert response.status_code == 200
        assert isinstance(response.json, dict)
        assert response.json["Message"] == "There are no products in inventory!"
    def test_add_product(self, client):
        """test add a new product enpoint"""
        response = client.post('/api/v1/products', data={
            "product_name": "playstation 4",
            "category" : "electronics",
            "quantity": 10,
            "product_unit_cost": 40000
        })
        # assert session.get("logged_in") == None
        assert response.status_code == 200
        assert isinstance(response.json, dict)
        assert response.json["Message"] == "New product added!"
    def test_get_one_product(self, client):
        """test get one client endpoint"""
        response = client.get('/api/v1/products/5')
        # assert session.get("logged_in") == None
        assert response.status_code == 200
        assert isinstance(response.json, dict)
        assert response.json["Message"] == "That product_id is not registered to any products!"
    def test_get_sales(self, client):
        """test get all sales endpoint"""
        response = client.get('/api/v1/sales')
        # assert session.get("logged_in") == None
        assert response.status_code == 200
        assert isinstance(response.json, dict)
        assert response.json["Message"] == "No sales records have been created!"
    def test_get_one_sale(self, client):
        """Test get one sale endpoint"""
        response = client.get('/api/v1/sales/2')
        # assert session.get("logged_in") == None
        assert response.status_code == 200
        assert isinstance(response.json, dict)
        assert response.json["Message"] == "No sales records have been created!"
    def test_add_sale(self, client):
        """Test make sale report endpoint"""
        response = client.post('/api/v1/sales', data={
            "attendant": "mufasa",
            "product": "Playstation 4",
            "quantity": 2,
        })
        # assert session.get("logged_in") == None
        assert response.status_code == 200
        assert isinstance(response.json, dict)
        assert response.json["Message"] == "There are no products in inventory!"
    def test_login(self, client):
        """test login endpoint"""
        response = client.post('/api/v1/login', data={
            "username": "admin",
            "password": "superuser"
        })
        # assert session.get("logged_in") == None
        assert response.status_code == 200
        assert isinstance(response.json, dict)
        assert response.json["Message"] == "Login Successful!"
    def test_signup(self, client):
        """test signup endpoint"""
        response = client.post('/api/v1/login', data={
            "username": "mufasa", "password":"dennis"
        })
        # assert session.get("logged_in") == None
        assert response.status_code == 200
        assert isinstance(response.json, dict)
        assert response.json["Message"] == "You are not an admin!"
