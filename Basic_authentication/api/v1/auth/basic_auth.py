#!/usr/bin/env python3
"""
Module providing the BasicAuth class for basic authentication handling in the API.
It extends the Auth class with methods specific to Basic Authentication.
"""

from api.v1.auth.auth import Auth
from base64 import b64decode, binascii
from models.user import User
from typing import TypeVar, Tuple

class BasicAuth(Auth):
    """
    BasicAuth class for handling basic authentication.

    It includes methods for:
    - Extracting and decoding the Base64 part of the Authorization header.
    - Extracting user credentials from the decoded string.
    - Retrieving the user object based on email and password.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header.

        Args:
        - authorization_header (str): The authorization header.

        Returns:
        - str: The Base64 part of the header, or None if invalid.
        """
        if not authorization_header or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string.

        Args:
        - base64_authorization_header (str): Base64 encoded string.

        Returns:
        - str: Decoded string, or None if decoding fails.
        """
        if not base64_authorization_header or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_bytes = b64decode(base64_authorization_header)
        except binascii.Error:
            return None

        return decoded_bytes.decode("utf-8")

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts user email and password from the decoded string.

        Args:
        - decoded_base64_authorization_header (str): Decoded auth header.

        Returns:
        - Tuple[str, str]: Email and password, or (None, None) if invalid.
        """
        if not decoded_base64_authorization_header or ':' not in decoded_base64_authorization_header:
            return None, None

        return decoded_base64_authorization_header.split(':', 1)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieves the User instance based on email and password.

        Args:
        - user_email (str): User's email.
        - user_pwd (str): User's password.

        Returns:
        - User: User instance if credentials are valid, otherwise None.
        """
        if not user_email or not user_pwd or not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users or not users[0].is_valid_password(user_pwd):
            return None

        return users[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Overloads Auth to retrieve the User instance for a request.

        Args:
        - request: The Flask request object.

        Returns:
        - User: User instance if authenticated, otherwise None.
        """
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(auth_header)
        decoded_auth_header = self.decode_base64_authorization_header(base64_auth_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_auth_header)

        return self.user_object_from_credentials(user_email, user_pwd)
