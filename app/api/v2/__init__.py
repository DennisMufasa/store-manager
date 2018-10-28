"""Set up version 2 blueprint"""
# third-party imports
from flask import Blueprint
# v2 blueprint
v2_blueprint = Blueprint('v2', __name__, url_prefix='/api/v2')
# import views for version 2
from . import views
