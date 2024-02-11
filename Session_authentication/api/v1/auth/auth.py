#!/usr/bin/env python3
""" task3. Module to manage authentication
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """Class to manage
    the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns False - path and excluded_paths"""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """method that returns None - request
        will be the Flask request object
        """
        if request is None:
            return None

        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Module that returns None - request
        will be the Flask request object
        """
        return request

    def session_cookie(self, request=None):
        """Module that returns a cookie
        value from a request:"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
