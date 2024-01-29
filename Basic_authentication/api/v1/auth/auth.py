#!/usr/bin/env python3
"""
This Auth module handles authentication for the API. It includes methods for
determining if a path requires authentication, extracting the Authorization
header, and identifying the current user based on the request.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    The Auth class manages API authentication processes.
    It contains methods for path authentication requirement checks,
    Authorization header extraction, and current user identification.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.

        Args:
            path (str): The path to check against excluded paths.
            excluded_paths (List[str]): List of paths that
            don't require auth.

        Returns:
            bool: True if path requires authentication, False otherwise.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize paths to ensure consistent comparison
        normalized_excluded = [
            p[:-1] if p.endswith('/') else p for p in excluded_paths]
        normalized_path = path[:-1] if path.endswith('/') else path

        return normalized_path not in normalized_excluded

    def authorization_header(self, request=None) -> str:
        """
        Extracts the Authorization header from a request.

        Args:
            request: The Flask request object.

        Returns:
            str: The value of the Authorization header, or None if absent.
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder for current user identification (to be implemented).

        Args:
            request: The Flask request object.

        Returns:
            TypeVar('User'): The current user object,
            or None if not implemented.
        """
        return None
