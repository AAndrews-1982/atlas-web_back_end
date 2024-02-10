#!/usr/bin/env python3
""" handles all routes for the views for Session authentication """
from flask import abort, jsonify, request
from models.user import User
from api.v1.views import app_views
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> str:
    """Method that handle all sessionS authentication login """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    if not User().search({'email': email}):
        return jsonify({"error": "no user found for this email"}), 404
    user = User().search({'email': email})[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        response = jsonify(user.to_json())
        response.set_cookie(getenv('SESSION_NAME'), session_id)
        return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """
    Task8.  manage route DELETE /api/v1/auth_session/logout
    """
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if destroy_session is False:
        abort(404)
    else:
        return jsonify({}), 200
