#!/usr/bin/env python3
"""
This module configures and initializes the Flask application for the API.
It sets up CORS (Cross-Origin Resource Sharing),
registers blueprints for routing,
and configures authentication mechanisms based on environment variables.
"""

from os import getenv
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

app = Flask(__name__)
app.register_blueprint(app_views)

# Enable CORS for all routes under '/api/v1/*'
# with origins allowed from anywhere
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Dynamically load the authentication mechanism
# based on the AUTH_TYPE environment variable
auth_type = os.getenv("AUTH_TYPE", "auth")
if auth_type == "basic_auth":
    auth = BasicAuth()
else:
    auth = Auth()


@app.before_request
def before_request_func():
    """
    Before request processing to implement authentication
    and authorization checks.

    This function runs before each request to the API and
    applies the following checks:
    - If `auth` is None, it bypasses authentication.
    - It checks whether the current path is exempt from authentication.
    - Validates the presence of an 'Authorization' header,
        aborting with a 401 status if missing.
    - Checks user authentication and aborts with a 403
    status if the user is not authorized.
    """
    if auth is None:
        return
    exempt_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                    '/api/v1/forbidden/']
    if not auth.require_auth(request.path, exempt_paths):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Error handler for 404 Not Found.

    This function is invoked when a request is made to a non-existent endpoint.
    It returns a JSON response with an error message and
    a 404 HTTP status code.

    Parameters:
    - error: Flask error object for the not found error.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error):
    """
    Error handler for 401 Unauthorized.

    This function is called when a request is made
    without valid authentication credentials.
    It returns a JSON response with an error message and a
    401 HTTP status code.

    Parameters:
    - error: Flask error object for the unauthorized error.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Error handler for 403 Forbidden.

    This function is triggered when a user tries to access
    a resource they do not have
    permission for. It returns a JSON response with an
    error message and a 403 HTTP status code.

    Parameters:
    - error: Flask error object for the forbidden error.
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    # Run the Flask app with host and port retrieved from environment
    # variables or defaults
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
