from flask import Flask


from .api import api
from .home import home
from .arcadiaApp import arcadiaApp

def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False,
                template_folder="templates", static_folder="global_static")


    with app.app_context():
        from . import db # noqa

        # db.init_db(); db.seed_db() 
        app.secret_key = "SUPERSECRETKEY...or not?"

        app.register_blueprint(home.home_bp)
        app.register_blueprint(api.api_bp, url_prefix="/api")
        app.register_blueprint(arcadiaApp.app_bp, url_prefix="/app")

        return app