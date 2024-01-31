#!/usr/bin/env python3
"""
This module implements a basic authentication class for a Flask application.
It provides mechanisms to determine if a request to a specific path requires
authentication, to retrieve the authorization header from a request, and
to identify the current user based on the request context.
"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')  # Generic type for user objects


class Auth():
    """
    A class to manage API authentication. This class provides methods to check
    if a request path requires authentication, to extract the authorization
    header from requests, and to identify the current user.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication based on a list
        of paths that are excluded from authentication.

        Args:
            path: The path to check for authentication requirement.
            excluded_paths: A list of paths that do not require authentication.

        Returns:
            True if the path requires authentication, False otherwise.
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        # Normalize the path to ensure consistency in comparison
        path += '/' if path[-1] != '/' else ''
        # Path does not require auth if it's in the list of excluded paths
        return not any(path == ep or path.startswith(ep)
                       for ep in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the given request.

        Args:
            request: The Flask request object from which to retrieve the
                     Authorization header. If not provided, defaults to None.

        Returns:
            The value of the Authorization header if present, None otherwise.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method for identifying the current user from the request.
        This method should be implemented in subclasses to provide the actual
        mechanism for user identification.

        Args:
            request: The Flask request object, which could be used to identify
                     the current user. Defaults to None.

        Returns:
            None. Should be overridden to return the current user object.
        """
        return None
