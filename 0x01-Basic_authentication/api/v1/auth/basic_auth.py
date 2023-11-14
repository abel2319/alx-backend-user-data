#!/usr/bin/env python3
"""6. Basic auth
"""
from api.v1.auth.auth import Auth
import base64
from flask import request
from models.user import User
from typing import List, TypeVar


class BasicAuth(Auth):
    """Basic auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if not authorization_header or\
            not isinstance(authorization_header, str) or\
                not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Decode base64 authorization header
        """
        if not base64_authorization_header or\
                not isinstance(base64_authorization_header, str):
            return None

        try:
            b64 = base64_authorization_header.encode('utf-8')
            return base64.b64decode(b64).decode('utf-8')
        except Exception:
            return

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """returns the user email and password from
        the Base64 decoded value.
        """
        if not decoded_base64_authorization_header or\
            not isinstance(decoded_base64_authorization_header, str) or\
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        decoded_b64 = decoded_base64_authorization_header.split(':')
        return (decoded_b64[0],
                ":".join(decoded_b64[1:]))

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on
        his email and password.
        """
        if not user_email or not isinstance(user_email, str) or\
                not user_pwd or not isinstance(user_pwd, str):
            return None

        try:
            usr = User.search({"email": user_email})
        except Exception as e:
            return None

        if not usr or len(usr) == 0:
            return None

        for u in usr:
            if u.is_valid_password(user_pwd):
                return u

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request
        """
        auth = self.authorization_header(request)
        auth = self.extract_base64_authorization_header(auth)
        auth = self.decode_base64_authorization_header(auth)
        auth = self.extract_user_credentials(auth)
        user = self.user_object_from_credentials(auth[0], auth[1])
        return user
