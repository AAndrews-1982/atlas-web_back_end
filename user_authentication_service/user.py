#!/usr/bin/env python3
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
        reset_token (str): Token used for resetting the user's password, can be null.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
    
