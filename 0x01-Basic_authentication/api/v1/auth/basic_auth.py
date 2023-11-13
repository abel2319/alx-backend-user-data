#!/usr/bin/env python3
"""6. Basic auth
"""
from api.v1.auth.auth import Auth
from flask import request
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
