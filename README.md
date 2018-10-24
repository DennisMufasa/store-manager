# store-manager  [![Build Status](https://travis-ci.org/DennisMufasa/store-manager.svg?branch=develop)](https://travis-ci.org/DennisMufasa/store-manager) [![Coverage Status](https://coveralls.io/repos/github/DennisMufasa/store-manager/badge.svg?branch=develop)](https://coveralls.io/github/DennisMufasa/store-manager?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/68fe4d63a01677d4799a/maintainability)](https://codeclimate.com/github/DennisMufasa/store-manager/maintainability)
Vew the app pages <a href="https://dennismufasa.github.io/store-manager/templates/">here</a><br>.
An app that manages a single store with an admin and store attendant access levels.


App still under construction

## How to manually run this app
1. Clone this repository into your local machine
2. Navigate to the folder store-manager. `cd store-manager`
3. Checkout develop branch. `git checkout develop`
4. While virtualenv is active: do `export FLASK_APP=run.py`, `export FLASK_ENV=development`, `export DEBUG=1`
5. Run the app by `flask run`
6. Test endpoints on postman

## alternatively?!
1. Visit `https://storemanager-api-heroku.herokuapp.com/` but add a route e.g. after the last '/' add `api/v1/products` at the end to test       the endpoints on Heroku.
2. Visit the url on postman rather tha a browser for the sake of performing POST request.

## Background information
Assuming you have created you won virtual environment by `python3 -m venv env`, install project dependencies from requirements.txt by `pip install -r requirements.txt`
### 1. Navigating the app
    - Login into the app at POST-`/api/v1/login`:
    - use these credentials {"username":"admin", "password":"superuser"}
    - create a few products by POSTing it via POST -`/api/v1/sales`.
    - add a new attendant by POSTing them via POST -`/api/v1/admin_add_user`
    - logout of the app at `/api/v1/logout`
    - login as the created user and make sales
    - products should be visible for all users at GET-`/api/v1/products`

### 2. user credentials to place in request body to login
        {"username":"your_user_name", "password":"your_password"}

### 3. product details to place in request body to add product
        {"product_name": "name of new product",
        "product_category": "name of new product",
        "product_quantity": "name of new product",
        "product_unit_cost": "name of new product"}

### 4. sale details to place in request body to add sale
        {"product": "product name",
        "quantity": "product quantity"}

### 5. attendant details to place in request body to add users
        {"email": "new user email",
        "username": "new user name",
        "password": "new user password",
        "role": "new user role"}

### 6. Edit details of products
        edit category - {"name": "product_name", "category": "new category"}
        edit unit cost - {"name": "product_name", "cost": "new product unit cost"}
        edit total available quantity - {"name": "product_name", "quantity": "number of items to add"}

### 7. editing user role
        Pass user_id as a request parameter at `/api/v1/edit/<int:user_id>


### NB. All headers contain `Content-type` set to `application/json`.
###    Get the documentation from <a href="https://documenter.getpostman.com/view/3964097/RWgwQaqV">here</a>
