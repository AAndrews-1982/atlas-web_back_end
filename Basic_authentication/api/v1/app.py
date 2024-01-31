#!/usr/bin/env python3
"""
This module sets up the Flask application and its routes, integrating CORS
(Cross-Origin Resource Sharing) and authentication mechanisms. It defines
error handlers and a before_request function to manage access control and
authenticate requests.
"""

from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from os import getenv

# Initialize Flask application
app = Flask(__name__)
app.register_blueprint(app_views)

# Setup CORS with wildcard origins for the API routes
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize authentication variable
auth = None

# Determine authentication type based on environment variable and instantiate
if getenv("AUTH_TYPE") == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def before_request() -> str:
    """
    Function executed before each request to enforce authentication and
    authorization checks except for specific paths.

    It verifies the request's path against a list of paths that do not require
    authentication. If authentication is required, it checks for valid
    authorization headers and whether the current user is accessible.
    """
    if auth is None:
        return None

    # Paths that do not require authentication
    check_pathlist = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    # If path requires auth and either auth header or current user is missing,
    # abort the request with appropriate error code
    if not (auth.require_auth(request.path, check_pathlist)):
        return

    if (auth.authorization_header(request)) is None:
        abort(401)

    if (auth.current_user(request)) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """Error handler for 404 Not Found responses."""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Error handler for 401 Unauthorized responses."""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Error handler for 403 Forbidden responses."""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    # Run the Flask application with host and port settings from environment
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
