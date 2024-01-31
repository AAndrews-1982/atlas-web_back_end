#!/usr/bin/env python3
"""
This module defines the BasicAuth class, extending the Auth class for handling
Basic Authentication in a Flask application. It includes methods for extracting
and decoding Base64 encoded credentials from the Authorization header, and
retrieving the corresponding user object.
"""

from api.v1.auth.auth import Auth
from base64 import b64decode, binascii
from models.user import User
from typing import TypeVar

UserType = TypeVar('User')  # Generic type for user objects


class BasicAuth(Auth):
    """
    BasicAuth class for handling Basic Authentication.

    This class provides methods to extract and decode Base64 encoded
    credentials from the Authorization header and to retrieve the user
    object associated with these credentials.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic
        Authentication.

        Args:
            authorization_header: The complete Authorization header value.

        Returns:
            The Base64 encoded portion of the Authorization header, or None
            if the header is not a valid Basic Authentication header.
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 encoded string from the Authorization header.

        Args:
            base64_authorization_header: The Base64 encoded credentials.

        Returns:
            The decoded string (typically 'username:password'), or None if
            the string cannot be decoded.
        """
        if base64_authorization_header is None:
            return None

        try:
            decoded_bytes = b64decode(base64_authorization_header)
        except binascii.Error:
            return None

        return decoded_bytes.decode("utf-8")

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user email and password from the decoded Base64 string.

        Args:
            decoded_base64_authorization_header: The decoded credentials
            string.

        Returns:
            A tuple containing the user email and password, or (None, None) if
            the credentials cannot be extracted.
        """
        if decoded_base64_authorization_header is None:
            return None, None

        return decoded_base64_authorization_header.split(':', 1)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> UserType:
        """
        Retrieves the User instance based on provided email and password.

        Args:
            user_email: The email of the user.
            user_pwd: The password of the user.

        Returns:
            The User instance if credentials are valid and user exists, None
            otherwise.
        """
        if user_email is None or user_pwd is None:
            return None

        users = User.search({'email': user_email})
        if not users or not users[0].is_valid_password(user_pwd):
            return None

        return users[0]

    def current_user(self, request=None) -> UserType:
        """
        Overloads Auth's current_user method to retrieve the User instance
        for a request using Basic Authentication.

        Args:
            request: The Flask request object.

        Returns:
            The User instance if the request contains valid credentials, None
            otherwise.
        """
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        decoded_header = self.decode_base64_authorization_header(
            self.extract_base64_authorization_header(auth_header)
        )
        user_email, user_pwd = self.extract_user_credentials(decoded_header)

        return self.user_object_from_credentials(user_email, user_pwd)
