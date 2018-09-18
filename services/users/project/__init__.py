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


"""
# Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

# Routes
@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({'status': 'success', 'message': 'pong!'})
"""
