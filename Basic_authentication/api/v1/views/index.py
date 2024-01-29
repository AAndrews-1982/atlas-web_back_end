#!/usr/bin/env python3
"""
This module defines routes for basic views in the API, including status
checks and error simulations. Each route is associated with an HTTP method
and returns a specific response.
"""

from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    Returns the current status of the API.

    Route: GET /api/v1/status
    This endpoint returns a JSON object indicating the API's operational
    status.

    Returns:
        JSON object with the key 'status' set to 'OK'.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    Returns the count of various objects in the API.

    Route: GET /api/v1/stats
    This endpoint aggregates data from different models (e.g., User) and
    returns a count of each object type.

    Returns:
        JSON object containing counts of various object types.
    """
    from models.user import User
    stats = {'users': User.count()}
    return jsonify(stats)


@app_views.route("/unauthorized", methods=["GET"], strict_slashes=False)
def test_unathourized() -> str:
    """
    Simulates an unauthorized access error.

    Route: GET /api/v1/unauthorized
    This endpoint triggers a 401 Unauthorized error to simulate scenarios
    where access is attempted without proper authentication.

    Returns:
        Triggers an abort with a 401 Unauthorized HTTP status code.
    """
    return abort(401)


@app_views.route("/forbidden", methods=["GET"], strict_slashes=False)
def forbidden() -> str:
    """
    Simulates a forbidden access error.

    Route: GET /api/v1/forbidden
    This endpoint triggers a 403 Forbidden error to simulate scenarios
    where access is denied even with authentication.

    Returns:
        Triggers an abort with a 403 Forbidden HTTP status code.
    """
    return abort(403)
