#!/usr/bin/env python3
""" Module of Users views for a Flask API.
"""

from flask import abort, jsonify, request
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """
    Retrieves a list of all User objects in JSON format.

    Returns:
        - JSON list of all users.
    """
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """
    Retrieves a single User object in JSON format.

    Args:
        user_id: The ID of the user, or 'me' for current user.

    Returns:
        - JSON representation of the user.
        - 404 error if the user does not exist.
    """
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_json())

    if user_id is None:
        abort(404)

    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """
    Deletes a User object.

    Args:
        user_id: The ID of the user to delete.

    Returns:
        - Empty JSON on success.
        - 404 error if the user does not exist.
    """
    if user_id is None:
        abort(404)

    user = User.get(user_id)
    if user is None:
        abort(404)

    user.remove()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """
    Creates a new User object.

    JSON body should contain:
        - email
        - password
        - last_name (optional)
        - first_name (optional)

    Returns:
        - JSON representation of the new user.
        - 400 error on invalid input or creation failure.
    """
    try:
        request_json = request.get_json()
    except Exception:
        return jsonify({'error': "Wrong format"}), 400

    if not request_json:
        return jsonify({'error': "Invalid JSON"}), 400

    email = request_json.get("email")
    password = request_json.get("password")
    if not email:
        return jsonify({'error': "email missing"}), 400
    if not password:
        return jsonify({'error': "password missing"}), 400

    try:
        user = User(email=email, password=password,
                    first_name=request_json.get("first_name"),
                    last_name=request_json.get("last_name"))
        user.save()
        return jsonify(user.to_json()), 201
    except Exception as e:
        return jsonify({'error': f"Can't create User: {e}"}), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """
    Updates a User object.

    Args:
        user_id: The ID of the user to update.

    JSON body should contain (all optional):
        - last_name
        - first_name

    Returns:
        - JSON representation of the updated user.
        - 404 error if the user does not exist.
        - 400 error on invalid input.
    """
    if user_id is None:
        abort(404)

    user = User.get(user_id)
    if user is None:
        abort(404)

    try:
        request_json = request.get_json()
    except Exception:
        return jsonify({'error': "Wrong format"}), 400

    if not request_json:
        return jsonify({'error': "Invalid JSON"}), 400

    user.first_name = request_json.get('first_name', user.first_name)
    user.last_name = request_json.get('last_name', user.last_name)
    user.save()
    return jsonify(user.to_json()), 200
