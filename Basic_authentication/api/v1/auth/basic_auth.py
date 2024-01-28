#!/usr/bin/env python3
"""
This BasicAuth module is designed for handling basic HTTP authentication
in a Flask application. It extends the functionalities of the Auth class
to support authentication using Base64 encoded credentials.
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar, Tuple
import base64

UserType = TypeVar('User')


class BasicAuth(Auth):
    """
    BasicAuth class for basic HTTP authentication.
    Inherits from Auth and implements methods for handling
    basic authentication mechanisms.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 encoded part from the Authorization header.

        Args:
        authorization_header (str): The full Authorization header.

        Returns:
        str: The Base64 encoded part, or None if invalid.
        """
        if authorization_header is None or \
           not isinstance(authorization_header, str) or \
           not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 encoded part of the Authorization header.

        Args:
        base64_authorization_header (str): The Base64 encoded part.

        Returns:
        str: Decoded string, or None if decoding fails.
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
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts user credentials from the decoded Base64 string.

        Args:
        decoded_base64_authorization_header (str): Decoded credentials.

        Returns:
        Tuple[str, str]: User email and password, or (None, None) if invalid.
        """
        if decoded_base64_authorization_header is None or \
           not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> UserType:
        """
        Retrieves the User instance based on email and password.

        Args:
        user_email (str): The email of the user.
        user_pwd (str): The password of the user.

        Returns:
        UserType: User instance if valid, otherwise None.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
