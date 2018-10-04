# Configures a route to /users/ping for testing purposes

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
import os

# Instantiate the db
db = SQLAlchemy()

# Instantiate the Debug Toolbar
toolbar = DebugToolbarExtension()


def create_app(script_info=None):

    # Instantiate the app
    app = Flask(__name__)

    # Set configurations
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # Instantiate the database
    db.init_app(app)

    # Instantiate the Debug Toolbar
    toolbar.init_app(app)

    # Register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # Shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
