#!/usr/bin/env python3
"""BasicAuth class module for API authentication."""

from .auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class for API authentication."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts Base64 part of the Authorization header."""
        if isinstance(authorization_header, str) and \
           authorization_header.startswith('Basic '):
            return authorization_header[6:]
        return None

    def decode_base64_authorization_header(self,
                                           base64_auth_header: str) -> str:
        """Decodes a Base64 string."""
        try:
            return base64.b64decode(base64_auth_header.encode('utf-8')).decode(
                'utf-8') if isinstance(base64_auth_header, str) else None
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_auth_header: str) -> (str, str):
        """Extracts user credentials from decoded header."""
        if isinstance(decoded_auth_header, str) and ':' in decoded_auth_header:
            return tuple(decoded_auth_header.split(':', 1))
        return None, None

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str):
        """Returns User instance based on email and password."""
        if isinstance(user_email, str) and isinstance(user_pwd, str):
            users = User.search({'email': user_email})
            if users and users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None):
        """Retrieves the User instance for a request."""
        auth_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        user_email, user_pwd = self.extract_user_credentials(
            decoded_auth_header)
        return self.user_object_from_credentials(user_email, user_pwd)
