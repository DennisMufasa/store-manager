"""Setting up v1 blueprint"""
from flask import Blueprint
# v1 blueprint
v1_bp = Blueprint('v1', __name__, url_prefix='/api/v1')
# local import
from . import views
