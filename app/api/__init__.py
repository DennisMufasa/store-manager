"""Setting up the application"""
# system imports
import os
# third-party imports
from flask import Flask
#local import
from instance.config import configuration
def create_app(config):
    """Application factory"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration[config])
    app.secret_key = os.urandom(24)
    # register blueprints
    from . v1 import v1_blueprint
    from . v2 import v2_blueprint
    app.register_blueprint(v1_blueprint)
    app.register_blueprint(v2_blueprint)
    return app
