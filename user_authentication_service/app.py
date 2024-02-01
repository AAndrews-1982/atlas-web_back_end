#!/usr/bin/env python3
"""
Flask app with a single GET route ("/") that returns
a JSON payload using flask.jsonify.
"""

from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome():
    """Return a Welcome message in JSON format."""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    Register a user.
    The method implements the endpoint to register a user.
    Returns:
        JSON payload with email and user creation message.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    Login function to handle POST requests on '/sessions'.
    Validates login credentials and creates a session.
    Returns:
        JSON payload with email and login message.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Handle logout requests on '/sessions'.
    Deletes the user's session and redirects to the home page.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        return jsonify({"error": "Invalid session ID"}), 403

    AUTH.destroy_session(user)
    return redirect(url_for('home'))


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """
    Respond to GET requests on '/profile'.
    Returns the user's profile if the session is valid.
    """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200

    abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> str:
    """
    Handle POST requests on '/reset_password'.
    Generates and returns a password reset token.
    """
    try:
        email = request.form.get('email')
        if email:
            token = AUTH.get_reset_password_token(email)
            return jsonify({"email": email, "reset_token": token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """
    Update the password via PUT requests on '/reset_password'.
    Args:
        "email", "reset_token", and "new_password".
    Returns:
        Confirmation of password update in JSON format.
    """
    email = request.form.get('email')
    new_pwd = request.form.get('new_password')
    token = request.form.get('reset_token')
    try:
        AUTH.update_password(token, new_pwd)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
