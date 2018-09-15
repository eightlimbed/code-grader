# Configures a route to /users/ping for testing purposes

from flask import Flask, jsonify

# Instantiate the app
app = Flask(__name__)

# Pull in the configuration (testing, dev, prod)
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({'status': 'success', 'message': 'pong!'})
