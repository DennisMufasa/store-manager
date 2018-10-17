"""Setting up the application"""
# third-party imports
from flask import Flask
#local import
from instance.config import configuration
def create_app(config):
    """Application factory"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration[config])
    # register blueprint
    from .v1 import v1_bp
    app.register_blueprint(v1_bp)
    return app
