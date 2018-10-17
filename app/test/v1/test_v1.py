"""Tests for vesrion 1 of my APIs"""
# third-party import
import pytest
from flask import url_for
class Test_view:
    """Tests endpoints"""
    def test_get_products(self, client):
        """test get all products endpoint"""
        response = client.get('/api/v1/products')
        assert response.status_code == 200
    def test_add_product(self, client):
        """test add a new product enpoint"""
        response = client.post('/api/v1/products', data={
            "name": "machete",
            "cost": 1000
        })
        assert response.status_code == 201
    def test_get_one_product(self, client):
        """test get one client endpoint"""
        response = client.get('/api/v1/products/1')
        assert response.status_code == 200
    def test_get_sales(self, client):
        """test get all sales endpoint"""
        response = client.get('/api/v1/sales')
        assert response.status_code == 200
    def test_get_one_sale(self, client):
        """Test get one sale endpoint"""
        response = client.get('/api/v1/sales/1')
        assert response.status_code == 200
    def test_add_sale(self, client):
        """Test make sale report endpoint"""
        response = client.post('/api/v1/sales', data={
            "name": "machette",
            "qty": 2,
            "cost": 1000
        })
        assert response.status_code == 201
    def test_login(self, client):
        """test login endpoint"""
        response = client.post('/api/v1/login', data={
            "user": "mufasa",
            "password": "dfghbjnk"
        })
        assert response.status_code == 201
    def test_signup(self, client):
        """test signup endpoint"""
        response = client.post('/api/v1/login', data={
            "user": "mufasa",
            "password": "dfghbjnk"
        })
        assert response.status_code == 201
