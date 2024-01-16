#!/usr/bin/env python3
"""3. Auth class"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')  # Define a TypeVar for User


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a particular path
        """
        return False  # This will be implemented later

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
