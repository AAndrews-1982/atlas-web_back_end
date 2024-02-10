#!/usr/bin/env python3
"""
SessionAuth Class, creates new authentication
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Session Authentication class """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Method that creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method that hat returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Method that returns a User
        instance based on a cookie_value"""
        cookie_value = self.session_cookie(request)
        if cookie_value is None:
            return None
        user_ID = self.user_id_for_session_id(cookie_value)
        return User.get(user_ID)

    def destroy_session(self, request=None):
        """Method that that deletes
        the user session / logout:"""
        if request is None:
            return False
        cookieid = self.session_cookie(request)
        if not cookieid:
            return False
        user_id = self.user_id_for_session_id(cookieid)
        if not user_id:
            return False
        del self.user_id_by_session_id[cookieid]
        return True
