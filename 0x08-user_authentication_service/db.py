#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class"""
    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''new user'''
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Returns first row found in users table based on keyword args """

        """ Handle invalid requests """
        if not kwargs:
            raise InvalidRequestError

        users_columns = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
            ]

        for arg in kwargs:
            if arg not in users_columns:
                raise InvalidRequestError

        """ Search table for user """

        search_user = self._session.query(User).filter_by(**kwargs).first()

        if search_user:
            return search_user
        else:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Finds user record and updates attributes """

        user_to_update = self.find_user_by(id=user_id)

        users_columns = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
            ]

        for k, v in kwargs.items():
            if k in users_columns:
                setattr(user_to_update, k, v)
            else:
                raise ValueError

        self._session.commit()
