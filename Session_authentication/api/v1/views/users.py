#!/usr/bin/env python3
"""
This module defines view functions for user-related actions, including
listing, retrieving, creating, deleting, and updating user records. Each
function is mapped to a specific HTTP method and route, with JSON responses
that conform to RESTful standards.
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """
    Retrieves a list of all user records.

    Returns:
        - JSON list of all users.
    """
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """
    Retrieves a single user record by ID. Special 'me' ID for current user.

    Parameters:
        - user_id: ID of the user or 'me' for the current user.

    Returns:
        - JSON representation of the user.
        - 404 error if user ID not found or 'me' with no current user.
    """
    if user_id is None or (user_id == 'me' and request.current_user is None):
        abort(404)
    if user_id == 'me':
        return jsonify(request.current_user.to_json())
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """
    Deletes a user record by ID.

    Parameters:
        - user_id: ID of the user to delete.

    Returns:
        - Empty JSON response if deletion successful.
        - 404 error if user ID not found.
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
    Creates a new user record from JSON request data.

    Expected JSON keys:
        - email (required)
        - password (required)
        - last_name (optional)
        - first_name (optional)

    Returns:
        - JSON representation of the created user.
        - 400 error if creation fails due to missing data or format issues.
    """
    try:
        rj = request.get_json()
    except Exception:
        return jsonify({'error': "Wrong format"}), 400

    error_msg = None
    if rj is None:
        error_msg = "Wrong format"
    elif not rj.get("email"):
        error_msg = "email missing"
    elif not rj.get("password"):
        error_msg = "password missing"

    if error_msg:
        return jsonify({'error': error_msg}), 400

    try:
        user = User()
        user.email = rj.get("email")
        user.password = rj.get("password")
        user.first_name = rj.get("first_name", "")
        user.last_name = rj.get("last_name", "")
        user.save()
        return jsonify(user.to_json()), 201
    except Exception as e:
        return jsonify({'error': f"Can't create User: {e}"}), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """
    Updates a user record by ID based on JSON request data.

    Parameters:
        - user_id: ID of the user to update.

    Expected JSON keys (all optional):
        - last_name
        - first_name

    Returns:
        - JSON representation of the updated user.
        - 400 error if update fails due to missing user ID or bad format.
        - 404 error if user ID not found.
    """
    if user_id is None:
        abort(400)
    user = User.get(user_id)
    if user is None:
        abort(404)

    try:
        rj = request.get_json()
    except Exception:
        return jsonify({'error': "Wrong format"}), 400

    if rj is None:
        return jsonify({'error': "Wrong format"}), 400

    user.first_name = rj.get('first_name', user.first_name)
    user.last_name = rj.get('last_name', user.last_name)
    user.save()
    return jsonify(user.to_json()), 200
