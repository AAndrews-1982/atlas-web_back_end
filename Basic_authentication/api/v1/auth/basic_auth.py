#!/usr/bin/env python3
"""
Module: Basic Authentication
This module contains the BasicAuth class which
inherits from the Auth class.
It provides mechanisms for handling basic HTTP
authentication using Base64 encoding.
"""
from api.v1.auth.auth import Auth
from base64 import b64decode, binascii
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    Basic Authentication class.

    This class implements basic authentication methods.
    It extends the Auth class by adding specific methods
    for basic authentication, such as extracting and decoding
    Base64-encoded credentials from the Authorization header
    in HTTP requests.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 encoded part of the Authorization header.

        This method is responsible for isolating the Base64
        encoded portion of the Authorization header,
        which is expected to follow the format "Basic <encoded_string>".
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
        Decodes a Base64 encoded string.

        This method takes a Base64 encoded string and attempts to decode it.
        It is designed to handle the Base64 part of an authorization header.
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            decoded_bytes = b64decode(base64_authorization_header)
        except binascii.Error as err:
            return None

        return decoded_bytes.decode("utf-8")

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user email and password from a decoded Base64 string.

        This method is intended to parse the decoded
        Base64 string to extract the user's email and
        password, which are expected to be separated by a colon.
        """
        if (
            decoded_base64_authorization_header is None or not
            isinstance(decoded_base64_authorization_header, str)
        ):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieves a User instance based on provided email and password.

        This method uses the provided email and password to
        search for and authenticate a User. If a User with the given
        email exists and the password is correct, the
        corresponding User object is returned.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})

        if not users:
            return None

        user_instance = users[0]

        if not user_instance.is_valid_password(user_pwd):
            return None

        return user_instance

    def current_user(self, request=None) -> TypeVar('User'):
        """Overloads Auth's current_user method to retrieve the
            User instance for a request.
            This method is the entry point for authenticating
            a user based on the
            information available in the HTTP request. It processes
            the request's authorization header to extract, decode,
            and validate user credentials,
            ultimately retrieving the corresponding User object.
        """
        if request is None:
            request = request

        auth_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        user_email, user_pwd = self.extract_user_credentials(
            decoded_auth_header)

        return self.user_object_from_credentials(user_email, user_pwd)
