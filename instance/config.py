"""Application configuration"""
# system import
import os
class Config:
    """Base config class"""
    DEBUG = True
    SECRET = os.getenv('SECRET')
class Development(Config):
    """Development configurations"""
    DEBUG = True
class Testing(Config):
    """Testing configurations"""
    DEBUG = True
    TESTING = True
configuration = {
    "development": Development,
    "testing": Testing
}
