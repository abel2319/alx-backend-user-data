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

        return (decoded_base64_authorization_header.split(':')[0],
                decoded_base64_authorization_header.split(':')[1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on
        his email and password.
        """
        if not user_email or not isinstance(user_email, str) or\
                not user_pwd or not isinstance(user_pwd, str):
            return None

        usr = User.search({"email": user_email})
        if not usr or len(usr) == 0:
            return None

        if not usr[0].is_valid_password(user_pwd):
            return None

        return usr[0]
