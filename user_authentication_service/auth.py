#!/usr/bin/env python3
"""
Auth Module
This module provides authentication functionalities.
"""

import bcrypt
from db import DB
from uuid import uuid4
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    Hash a password string.

    Args:
        password (str): Plain text password.

    Returns:
        str: Hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generate a random UUID.

    Returns:
        str: Randomly generated UUID.
    """
    return str(uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.

    Methods handle user registration, login validation, session management,
    and password reset functionalities.
    """

    def __init__(self):
        """ Initialize Auth class with a database instance. """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Args:
            email (str): User's email.
            password (str): User's password.

        Returns:
            User: New User object.

        Raises:
            ValueError: If user already exists.
        """
        try:
            reg_user = self._db.find_user_by(email=email)
        except NoResultFound:
            passw = _hash_password(password)
            reg_user = self._db.add_user(email, passw)
            return reg_user
        else:
            raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login.

        Args:
            email (str): User's email.
            password (str): User's password.

        Returns:
            bool: True if login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Create a session for a user.

        Args:
            email (str): User's email.

        Returns:
            str: Session ID.
        """
        user = self._db.find_user_by(email=email)
        if user:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """
        Get a user by their session ID.

        Args:
            session_id (str): Session ID.

        Returns:
            str: User object.
        """
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except Exception:
                return ValueError

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a user's session.

        Args:
            user_id (int): User's ID.

        Returns:
            None
        """
        if user_id:
            try:
                self._db.find_user_by(user_id, session_id=None)
            except NoResultFound:
                None

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a password reset token.

        Args:
            email (str): User's email.

        Returns:
            str: Reset token.
        """
        if email:
            user = self._db.find_user_by(email=email)
            if email is None:
                raise ValueError
            user.reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=user.reset_token)
            return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update a user's password.

        Args:
            reset_token (str): Reset token.
            password (str): New password.

        Returns:
            None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user:
                password = _hash_password(password)
                self._db.update_user(user.id, hashed_password=password,
                                     reset_token=None)
        except NoResultFound:
            raise ValueError
