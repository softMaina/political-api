import os 

class Config(object):
    "Parent configuration class"
    DEBUG=True

class Development(Config):
    "Configuration for developement"
    DEBUG = True

class Production(Config):
    "Configurations for production"
    DEBUG = False
    TESTING = False

class Testing(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


config = {
    'development': Development,
    'production': Production,
     'testing': Testing
}