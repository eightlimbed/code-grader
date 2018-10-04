# Configures a route to /users/ping for testing purposes

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Instantiate the db
db = SQLAlchemy()


def create_app(script_info=None):
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    db.init_app(app)

    # Register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # Shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
