from flask import Flask


from .api import api
from .home import home


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False,
                template_folder="templates", static_folder="static")

    with app.app_context():

        app.register_blueprint(home.home_bp)
        app.register_blueprint(api.account_bp, url_prefix="/api")

        return app