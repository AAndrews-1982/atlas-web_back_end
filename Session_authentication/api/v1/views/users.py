#!/usr/bin/env python3
"""Module defines user-related API endpoints.

Supports listing, viewing, creating, deleting, and updating users.
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """GET /api/v1/users: Return all User objects as JSON."""
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """GET /api/v1/users/<user_id>: Return a User object as JSON.

    Returns 404 if User ID doesn't exist or 'me' without authentication.
    """
    if user_id is None or (user_id == 'me' and not request.current_user):
        abort(404)
    user = User.get(user_id) if user_id != 'me' else request.current_user
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """DELETE /api/v1/users/:id: Deletes a User, returns empty JSON on success.

    Returns 404 if the User ID doesn't exist.
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
    """POST /api/v1/users/: Creates a User from JSON body.

    Required fields: email, password. Optional: last_name, first_name.
    Returns User JSON or 400 if creation fails.
    """
    rj = request.get_json(silent=True)
    if rj is None:
        return jsonify({'error': "Wrong format"}), 400
    if not rj.get("email"):
        return jsonify({'error': "email missing"}), 400
    if not rj.get("password"):
        return jsonify({'error': "password missing"}), 400
    try:
        user = User()
        user.email = rj['email']
        user.password = rj['password']
        user.first_name = rj.get('first_name')
        user.last_name = rj.get('last_name')
        user.save()
        return jsonify(user.to_json()), 201
    except Exception as e:
        return jsonify({'error': f"Can't create User: {e}"}), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """PUT /api/v1/users/:id: Updates a User's details from JSON body.

    Optional JSON fields: last_name, first_name.
    Returns User JSON or 400/404 if update fails.
    """
    rj = request.get_json(silent=True)
    if user_id is None or rj is None:
        abort(400)
    user = User.get(user_id)
    if user is None:
        abort(404)
    if 'first_name' in rj:
        user.first_name = rj['first_name']
    if 'last_name' in rj:
        user.last_name = rj['last_name']
    user.save()
    return jsonify(user.to_json()), 200
