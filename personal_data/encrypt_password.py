#!/usr/bin/env python3
"""Encrypt Password Module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with a generated salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: Salted, hashed password.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates if a password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to check.

    Returns:
        bool: True if it matches, False otherwise.
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
