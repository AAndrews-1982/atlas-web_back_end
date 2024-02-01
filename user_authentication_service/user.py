#!/usr/bin/env python3
"""
This module defines the User model, which represents
a user in the database. It creates a table named 'users'
with various fields to store user information.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Base class for our class definitions
Base = declarative_base()


class User(Base):
    """
    A SQLAlchemy model named 'User'.

    This class represents a table named 'users' in the database.
    It is used to store user-related data.
    """
    __tablename__ = 'users'

    # Unique identifier for each user
    id = Column(Integer, primary_key=True)
    # User's email address
    email = Column(String(250), nullable=False)
    # User's hashed password
    hashed_password = Column(String(250), nullable=False)
    # Session ID for the user (can be null)
    session_id = Column(String(250), nullable=True)
    # Token for resetting password (can be null)
    reset_token = Column(String(250), nullable=True)
