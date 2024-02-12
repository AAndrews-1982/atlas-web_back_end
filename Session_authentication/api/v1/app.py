#!/usr/bin/env python3
"""
Defines routing for an API with authentication mechanisms and error handling.
It manages access and responses for unauthorized, forbidden, or not found
requests.
"""

from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
# Enable CORS for all origins on API v1 routes
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None

# Instantiate auth based on the AUTH_TYPE environment variable
if getenv("AUTH_TYPE") == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif getenv("AUTH_TYPE") == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.before_request
def before_request():
    """
    Middleware to run before each request. Checks if authentication is needed
    and validates it. Halts unauthorized or forbidden requests with appropriate
    error codes.
    """
    if auth is None:
        return None

    exempt_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                    '/api/v1/forbidden/', '/api/v1/auth_session/login/']

    if not auth.require_auth(request.path, exempt_paths):
        return
    if not auth.authorization_header(request) and
    not auth.session_cookie(request):
        abort(401)
    request.current_user = auth.current_user(request)
    if request.current_user is None:
        abort(403)


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Handles unauthorized requests with a 401 status code."""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Handles forbidden requests with a 403 status code."""
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """Handles not found requests with a 404 status code."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
