#!/usr/bin/env python3
"""
Defines the Flask application and its routes. It includes CORS setup for
handling cross-origin requests, authentication setup based on environment
variables, before request processing for authentication, and custom error
handlers for 401, 403, and 404 errors.
"""

from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
from os import getenv

# Initialize Flask application
app = Flask(__name__)
app.register_blueprint(app_views)  # Register the application views

# Setup CORS to allow all origins for API v1 routes
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize authentication system based on AUTH_TYPE environment variable
auth = None
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
    Runs before each request. Checks if authentication is required and verifies
    the current user's credentials. If authentication fails, returns 401 or 403
    """
    if auth is None:
        return None  # No authentication required

    # Paths that don't require authentication
    exempt_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                    '/api/v1/forbidden/', '/api/v1/auth_session/login/']

    if not auth.require_auth(request.path, exempt_paths):
        return  # Skip authentication for exempt paths

    # Verify authentication via headers or cookies
    if (not auth.authorization_header(request) and
            not auth.session_cookie(request)):
        abort(401)  # Unauthorized access

    request.current_user = auth.current_user(request)
    if request.current_user is None:
        abort(403)  # Forbidden access


@app.errorhandler(401)
def unauthorized(error):
    """Handles 401 Unauthorized errors by returning JSON response."""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """Handles 403 Forbidden errors by returning JSON response."""
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error):
    """Handles 404 Not Found errors by returning JSON response."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    # Run Flask application with host and port
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
