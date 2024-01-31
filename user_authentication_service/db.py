#!/usr/bin/env python3
"""
DB module
This module provides a class `DB` for interacting with a SQLite
database using SQLAlchemy. It allows for creating and managing
a database with user data.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

# Import Base and User models for database interaction.
from user import Base, User


class DB:
    """
    DB class for handling database operations.

    Attributes:
        _engine: A SQLAlchemy engine instance for database connections.
        __session: A private SQLAlchemy session for executing
        database operations.
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance.
        This method creates a new database engine
        and prepares the database schema.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        # Drop all tables in the database.
        Base.metadata.create_all(self._engine)
        # Create all tables in the database.
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object.
        Provides a SQLAlchemy session instance,
        creating it if it does not exist.

        Returns:
            A SQLAlchemy session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Save the user to the database.

        Args:
            email (str): The email address of the user.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The User object that was added to the database.
        """
        user_to_add = User(email=email, hashed_password=hashed_password)
        self._session.add(user_to_add)
        self._session.commit()
        return user_to_add

    def find_user_by(self, **keywords) -> User:
        """
        Takes in arbitrary keyword arguments and returns the
        first row found in the users table as filtered
        by the methods input arguments.

        Args:
            **keywords: Arbitrary number of keyword arguments.

        Returns:
            User: The first User object that matches
            the given criteria.

        Raises:
            NoResultFound: If no results are found in the query.
        """
        try:
            user = self.__session.query(User).filter_by(**keywords).first()
            if user is None:
                raise NoResultFound
            return user
        except InvalidRequestError:
            raise

    def update_user(self, user_id: int, **keywords) -> None:
        """
        Update the attributes of a user.

        Use find_user_by to locate the user to update, then update
        the users attributes as passed in the methods arguments
        then commit changes to the database.

        Args:
            user_id (int): The ID of the user to update.
            **keywords: Arbitrary number of keyword arguments
            representing the attributes to update.

        Returns:
            None

        Raises:
            ValueError: If a provided attribute key does not
            exist in the User model.
        """
        user = self.find_user_by(id=user_id)

        for key, value in keywords.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)

        self._session.commit()
        return None
