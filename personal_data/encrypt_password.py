#!/usr/bin/env python3
"""
Module: encrypt_password

Provides functionality for password encryption using bcrypt. Includes functions
for hashing and validating passwords.

Functions:
    hash_password(password: str) -> bytes
        Returns a salted, hashed password as a byte string.

    is_valid(hashed_password: bytes, password: str) -> bool
        Checks if a password matches a hashed password.
"""

import bcrypt


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Hashes a password with a generated salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: Salted, hashed password.
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
