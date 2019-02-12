import os

from flask import Flask
from instance.config import config
from app.utils.validator import return_error

# handle 405 errors
def handle_405_error(err):
    return return_error(405,"method not allowed")

# handle 404 errors
def handle_404_error(err):
    return return_error(404,"bad url format")

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.api.v1.views import party_views
    from app.api.v1.views import office_views


    app.register_blueprint(party_views.party_route)
    
    app.register_blueprint(office_views.office_route)

    # register 405 error handler
    app.register_error_handler(405,handle_405_error)
    app.register_error_handler(404,handle_404_error)


    return app