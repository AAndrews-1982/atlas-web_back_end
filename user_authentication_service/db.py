#!/usr/bin/env python3
"""
DB module for interacting with the database.
"""

from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


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

    Returns:
        User: The newly created User object with the
        specified email and hashed password.
    """
    new_user = User(email=email, hashed_password=hashed_password)
    self._session.add(new_user)
    self._session.commit()
    return new_user


def find_user_by(self, **kwargs) -> User:
    """
    Finds a user in the database based on specified criteria.

    This method queries for a User object matching given criteria, passed as
    arbitrary keyword arguments. It returns the first user
    that matches the query, useful for searching users by attributes
    like email, username, etc.


    Returns:
        User: The first User object found in the database
        matching the criteria.

    Raises:
        NoResultFound: If no User objects match the criteria in the database.
        InvalidRequestError: If the query criteria (kwargs) are invalid or
                             incorrectly formatted, such as an attribute
                             in kwargs not existing on the User model.
    """
    if not kwargs:
        raise InvalidRequestError

    user = self._session.query(User).filter_by(**kwargs).first()

    if user is None:
        raise NoResultFound

    return user
