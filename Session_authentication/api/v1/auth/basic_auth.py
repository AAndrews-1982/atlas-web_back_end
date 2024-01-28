#!/usr/bin/env python3
"""
This BasicAuth module is designed for handling basic HTTP authentication
in a Flask application. It extends the functionalities of the Auth class
to support authentication using Base64 encoded credentials.
"""
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import TypeVar
import base64


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
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or \
           not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieves a User instance based on email and password.

        This method validates the user's credentials against stored data.
        It first checks if the email and password are valid strings. Then, it
        looks up the user in the database by email. If the user is found, it
        verifies the password. If the credentials are valid, it returns the
        User instance; otherwise, it returns None.

        Args:
        user_email (str): Email of the user.
        user_pwd (str): Password of the user.

        Returns:
        The User instance if credentials are valid, None otherwise.
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
