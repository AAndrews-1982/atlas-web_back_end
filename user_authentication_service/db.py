#!/usr/bin/env python3
"""
DB module
This module provides a class `DB` for interacting
with a SQLite database using SQLAlchemy.
It allows for creating and managing a
database with user data.
"""
from user import Base, User
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB classfor handling database operations.
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """save the user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **keywords) -> User:
        """takes in arbitrary keyword arguments and returns
        the first row found in the users table as filtered
        by the method’s input arguments
        """
        try:
            user = self.__session.query(User).filter_by(**keywords).first()
            if user is None:
                raise NoResultFound
            return user
        except InvalidRequestError:
            raise

    def update_user(self, user_id: int, **keywords) -> None:
        """use find_user_by to locate the user to update, then
        will update the user’s attributes as passed in the
        method’s arguments then commit changes to the database"""
        user = self.find_user_by(id=user_id)

        for key, value in keywords.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)

        self._session.commit()
        return None
