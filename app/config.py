import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Other existing configurations

class DevelopmentConfig(Config):
    DEBUG = True
    # Additional development configurations

class ProductionConfig(Config):
    DEBUG = False
    # Additional production configurations

class TestingConfig(Config):
    TESTING = True

Config.UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads') 