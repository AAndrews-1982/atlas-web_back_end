#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


# Load authentication instance based on AUTH_TYPE
if getenv("AUTH_TYPE") == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()

elif getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def before_request_func():
    """ Filter each request to ensure authentication and authorization.

    - If the 'auth' object is None, no authentication is required.
    - The request is allowed through without authentication for certain paths
      specified in the 'exempt_paths' list.
    - If the request does not contain an 'Authorization' header, the server
      aborts with a 401 Unauthorized status.
    - If the 'Authorization' header is present but the user cannot be
      identified or authorized, the server aborts with a 403 Forbidden status.
    """
    if auth is None:
        return

    exempt_paths = ['/api/v1/status/',
                    '/api/v1/unauthorized/',
                    '/api/v1/forbidden/']
    if not auth.require_auth(request.path, exempt_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    request.current_user = auth.current_user(request)
    if request.current_user is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def unauthorized(error):
    """
    Error handler for 401 Unauthorized access.

    Invoked when an unauthorized access attempt is made on a protected endpoint
    without valid credentials. Responds with a JSON payload indicating the
    error and HTTP status code 401.

    Parameters:
    - error: Flask error object for the unauthorized access.

    Returns:
    - JSON response {"error": "Unauthorized"} with HTTP status code 401.
    """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
