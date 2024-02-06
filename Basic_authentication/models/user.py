#!/usr/bin/env python3
"""
This module defines views for User entities, allowing for operations such as
listing all users, viewing a single user, creating, deleting, and updating a
user via a RESTful API interface. It utilizes Flask for routing and handling
HTTP requests.
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """
    Handles GET request for listing all users.

    Returns:
        A JSON list of all User objects.
    """
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """
    Handles GET request for retrieving a specific user by ID.

    Args:
        user_id: The ID of the user to retrieve.

    Returns:
        A JSON representation of the User object if found,
        otherwise a 404 error if the user ID does not exist.
    """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """
    Handles DELETE request for deleting a specific user by ID.

    Args:
        user_id: The ID of the user to delete.

    Returns:
        An empty JSON response if the user has been correctly deleted,
        otherwise a 404 error if the user ID does not exist.
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
    Handles POST request for creating a new user.

    Expects a JSON body with user details, including required email and
    password fields, and optional last_name and first_name fields.

    Returns:
        A JSON representation of the created User object if successful,
        or a 400 error with an error message if the user cannot be created.
    """
    rj = None
    error_msg = None
    try:
        rj = request.get_json()
    except Exception:
        rj = None
    if rj is None:
        error_msg = "Wrong format"
    if error_msg is None and rj.get("email", "") == "":
        error_msg = "email missing"
    if error_msg is None and rj.get("password", "") == "":
        error_msg = "password missing"
    if error_msg is None:
        try:
            user = User()
            user.email = rj.get("email")
            user.password = rj.get("password")
            user.first_name = rj.get("first_name", "")
            user.last_name = rj.get("last_name", "")
            user.save()
            return jsonify(user.to_json()), 201
        except Exception as e:
            error_msg = f"Can't create User: {e}"
    return jsonify({'error': error_msg}), 400

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """
    Handles PUT request for updating a specific user by ID.

    Args:
        user_id: The ID of the user to update.

    Expects a JSON body with the fields to update, including optional
    last_name and first_name fields.

    Returns:
        A JSON representation of the updated User object if successful,
        a 400 error with an error message if the user cannot be updated,
        or a 404 error if the user ID does not exist.
    """
    if user_id is None:
        abort(400)
    user = User.get(user_id)
    if user is None:
        abort(400)
    rj = None
    try:
        rj = request.get_json()
    except Exception:
        rj = None
    if rj is None:
        return jsonify({'error': "Wrong format"}), 400
    user.first_name = rj.get('first_name', user.first_name)
    user.last_name = rj.get('last_name', user.last_name)
    user.save()
    return jsonify(user.to_json()), 200
