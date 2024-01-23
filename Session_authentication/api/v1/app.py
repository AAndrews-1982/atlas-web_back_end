#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None  # Initialize auth to None
AUTH_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE:
    from api.v1.auth.auth import Auth
    auth = Auth()  # Create an instance of Auth
else:
    from api.v1.auth.auth import Auth
    auth = Auth()  # Create an instance of Auth


@app.before_request
def before_request_func():
    """ Function to run before each request """
    if auth:
        excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                          '/api/v1/forbidden/']
        if not auth.require_auth(request.path, excluded_paths):
            return
        # Check for the presence of the Authorization header
        auth_header = auth.authorization_header(request)
        if auth_header is None:
            abort(401)  # Unauthorized if the header is missing

        # Retrieve the current user based on the Authorization header
        request.current_user = auth.current_user(request)
        if request.current_user is None:
            # Distinguish between a non-existent user and wrong password
            if auth.user_exists(request):
                abort(403)  # Forbidden if the user exists but wrong password
            else:
                abort(401)  # Unauthorized if the user doesn't exist


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
