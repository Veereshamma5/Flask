from flask import Flask
from app.models import DB, MIGRATE
from app.api.study_api import study_bp


def create_app(app_config):
    Flask_app = Flask(__name__)
    config = app_config()
    Flask_app.config.from_object(config)

    DB.init_app(Flask_app)
    MIGRATE.init_app(Flask_app, DB)
    # Register the blueprint
    Flask_app.register_blueprint(study_bp)
    return Flask_app
