#!/usr/bin/env python3
"""1. Empty session
"""
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import List, TypeVar
from uuid import uuid4


class SessionAuth(Auth):
    """ Session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id
        """
        if not user_id or not isinstance(user_id, str):
            return None

        id = str(uuid4())
        SessionAuth.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID
        """
        if not session_id or not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id, None)
    
    def current_user(self, request=None):
        """(overload) that returns a User instance based on a cookie value
        """
        session_name = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_name)
        user = User.get(user_id)
        return user
