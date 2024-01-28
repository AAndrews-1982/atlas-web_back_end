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
    BasicAuth class provides mechanisms for handling basic HTTP authentication.

    It inherits from the Auth class and implements additional methods specific
    to basic authentication, such as extracting and decoding credentials from
    the Authorization header.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 encoded credentials part from the Authorization header.

        Parameters:
        - authorization_header: The full value of the Authorization header received
          in the HTTP request.

        Returns:
        - The Base64 encoded part of the Authorization header, or None if the header
          is not valid or does not start with 'Basic '.
        """
        if authorization_header is None or \
           not isinstance(authorization_header, str) or \
           not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 encoded credentials from the Authorization header.

        Parameters:
        - base64_authorization_header: The Base64 encoded credentials part of the
          Authorization header.

        Returns:
        - The decoded string (typically 'username:password'), or None if the string
          cannot be decoded or is not valid Base64.
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
        Extracts the user email and password from the decoded Base64 authorization header.

        Parameters:
        - decoded_base64_authorization_header: The decoded credentials string from the
          Authorization header.

        Returns:
        - A tuple containing the user email and password, or (None, None) if the credentials
          cannot be extracted.
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
        Retrieves the User instance based on provided email and password.

        Parameters:
        - user_email: The email of the user.
        - user_pwd: The password of the user.

        Returns:
        - The User instance if the email and password are correct and match a user,
          or None if the credentials are invalid or the user does not exist.
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
