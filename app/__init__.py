import os

from flask import Flask

from instance.config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.api.v1.views import party_views
    from app.api.v1.views import office_views


    app.register_blueprint(party_views.party_route)
    
    app.register_blueprint(office_views.office_route)


    return app