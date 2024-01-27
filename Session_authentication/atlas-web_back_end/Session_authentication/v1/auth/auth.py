#!/usr/bin/env python3
"""3. Auth class"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')  # Define a TypeVar for User


class Auth:
    """Class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a particular path
        """
        if path is None or not excluded_paths:
            return True

        # Add a slash at the end of the path if not present for slash tolerance
        if path[-1] != '/':
            path += '/'

        # Check if the path is in excluded paths
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from a Flask request object
        """
        return None  # To be implemented

    def current_user(self, request=None) -> User:
        """
        Retrieves the current user from a Flask request object
        """
        return None  # To be implemented
