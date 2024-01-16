import logging
import logging.config
import time

from flasgger import Swagger
from flask import Flask

from app.logging_config import config as log_config
from app.models import DB, MIGRATE
from app.api.Learning_api import learning_bp
from app.mailers import mail

swagger_template = {
    'info': {
        'title': 'CDP App',
        'description': 'CDP App - An app to simplify the cdp process.',
        'version': '0.1',
        'contact': {
            'name': 'Seneca Global',
            'email': 'veereshamma.kake@senecaglobal.com'
        }
    },
    'components': {
        'securitySchemas': {
            'bearerAuth': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT'

            }
        }
    },
    'security': [
        {
            'bearerAuth': []
        }
    ]
}


def create_app(app_config):
    logging.config.dictConfig(log_config.LOGGING_CONF)
    logging.Formatter.converter = time.localtime

    flask_app = Flask(__name__, template_folder='email_templates')

    config = app_config()
    flask_app.config.from_object(config)

    # Swagger Configuration

    flask_app.config["SWAGGER"] = {
        'title': 'CDP App APIs',
        'openapi': '3.0.2',
        'uiversion': 3,
        "swagger_ui": True,
        'specs_route': '/swagger/'
    }

    # Create an object for Swagger
    unused_swagger = Swagger(flask_app, template=swagger_template)
    DB.init_app(flask_app)
    MIGRATE.init_app(flask_app, DB)
    # marshmallow.init_app(flask_app)
    mail.init_app(flask_app)
    flask_app.register_blueprint(learning_bp)
    return flask_app
