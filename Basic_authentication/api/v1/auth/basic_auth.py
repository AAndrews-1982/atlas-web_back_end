#!/usr/bin/env python3
"""
BasicAuth module for handling basic authentication.
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """
    BasicAuth class for basic HTTP authentication.
    Inherits from Auth and implements methods for handling
    basic authentication.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts Base64 encoded credentials from Authorization header.

        Parameters:
        - authorization_header: Full value of the Authorization header.

        Returns:
        - Base64 encoded credentials or None if invalid.
        """
        if authorization_header is None or \
                not isinstance(authorization_header, str) or \
                not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes Base64 encoded credentials from Authorization header.

        Parameters:
        - base64_authorization_header: Base64 encoded credentials.

        Returns:
        - Decoded credentials string or None if invalid.
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            return decoded_bytes.decode('utf-8')
        except (ValueError, TypeError, base64.binascii.Error):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user email and password from decoded credentials.

        Parameters:
        - decoded_base64_authorization_header: Decoded credentials.

        Returns:
        - Tuple of email and password, or (None, None) if invalid.
        """
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        return decoded_base64_authorization_header.split(':', 1)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieves User instance based on email and password.

        Parameters:
        - user_email: User's email.
        - user_pwd: User's password.

        Returns:
        - User instance or None if credentials are invalid.
        """
        if user_email is None or \
                not isinstance(user_email, str) or \
                user_pwd is None or \
                not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
