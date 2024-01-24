#!/usr/bin/env python3
"""
DB module for interacting with the database.
"""

from sqlalchemy.orm.session import Session
from user import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:
    """
    DB class for handling database operations.
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance.
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session


def add_user(self, email: str, hashed_password: str) -> User:
    """
    Add a new user to the database.

    Args:
        email (str): The email address of the user.
        hashed_password (str): The hashed password of the user.

    Returns:
        User: The newly created User object with the
        specified email and hashed password.
    """
    new_user = User(email=email, hashed_password=hashed_password)
    self._session.add(new_user)
    self._session.commit()
    return new_user