#!/usr/bin/env python3
"""
Module for defining the User model for user authentication service.

This module defines the User model used in the user authentication service,
including attributes for user identification and authentication.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User model for storing user details.

    Attributes:
        id (int): Unique identifier for the user, serves as the primary key.
        email (str): Email address of the user, cannot be null.
        hashed_password (str): Hashed password for the user, cannot be null.
        session_id (str): Session ID for the user, can be null.
        reset_token (str): Token used for resetting the
        user's password, can be null.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
