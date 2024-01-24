#!/usr/bin/env python3
""" Auth class """

from flask import request
from typing import List, TypeVar, Optional
import os
import base64

UserType = TypeVar('UserType')  # Define a TypeVar for User


class Auth():
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if authentication is required for a path """
        if path is None or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        return not any(ep.endswith('/') and path.startswith(ep)
                       for ep in excluded_paths)

    def authorization_header(self, request=None) -> Optional[str]:
        """ Retrieve Authorization header from a Flask request """
        if request:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> UserType:
        """ Retrieve the current user from a Flask request """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        encoded = auth_header.replace('Basic ', '', 1)
        decoded = base64.b64decode(encoded).decode('utf-8')
        username, password = decoded.split(':', 1)

        # Placeholder for user verification logic
        # Implement user verification here

        return None

    def session_cookie(self, request=None):
        """ Retrieve a session cookie from a Flask request """
        if request:
            session_name = os.getenv('SESSION_NAME',
                                     'your_default_session_name')
            return request.cookies.get(session_name)
        return None
