"""Configuration for tests"""
# third-party import
import pytest
# local import
from app.api import create_app
# fixture
@pytest.fixture
def app():
    app = create_app('testing')
    app.debug = True
    return app
