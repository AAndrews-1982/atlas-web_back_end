#!/usr/bin/env python3
"""
Auth module for handling authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the path requires authentication.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Ensure that all paths in excluded_paths end with '/'
        normalized_excluded = [
            p[:-1] if p.endswith('/') else p
            for p in excluded_paths
        ]

        # Normalize the input path in the same way
        normalized_path = path[:-1] if path.endswith('/') else path

        return normalized_path not in normalized_excluded

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header value from the request.
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user from the request.
        """
        return None
