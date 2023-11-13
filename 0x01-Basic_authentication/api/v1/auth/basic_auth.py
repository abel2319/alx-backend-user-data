#!/usr/bin/env python3
"""6. Basic auth
"""
from api.v1.auth.auth import Auth
import base64
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
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