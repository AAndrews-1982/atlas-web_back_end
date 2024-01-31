#!/usr/bin/env python3
"""
This module defines a class for managing authentication within an API,
including methods for determining if a request requires authentication,
retrieving the authorization header, and identifying the current user.
"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')  # Define a generic type for User


class Auth():
    """
    A class to manage API authentication processes, including verifying
    if certain paths require authentication, extracting authorization
    headers, and identifying the current user based on the request.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.

        Args:
            path: The path of the request.
            excluded_paths: A list of paths that do not require authentication.

        Returns:
            True if the path requires authentication, False otherwise.
        """
        if path is None or not excluded_paths:
            return True
        # Ensure path format is consistent by appending '/' if absent
        normalized_path = path if path.endswith('/') else path + '/'
        # Path is not required to authenticate if it's in the excluded_paths
        return not any(ep.endswith('/') and normalized_path.startswith(ep)
                       for ep in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.

        Args:
            request: The Flask request object.

        Returns:
            The value of the Authorization header, or None if not present.
        """
        if request and 'Authorization' in request.headers:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method for obtaining the current user.

        Args:
            request: The Flask request object.

        Returns:
            Currently, this method returns None. It should be overridden
            to provide actual user identification based on the request.
        """
        return None
