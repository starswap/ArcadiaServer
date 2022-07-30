from flask import Flask


from .api import api
from .home import home
from .account import account
from .arcadiaApp import arcadiaApp

def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False,
                template_folder="templates", static_folder="global_static")

    with app.app_context():

        app.register_blueprint(home.home_bp)
        app.register_blueprint(api.api_bp, url_prefix="/api")
        app.register_blueprint(account.account_bp, url_prefix="/account")
        app.register_blueprint(arcadiaApp.app_bp, url_prefix="/app")

        return app