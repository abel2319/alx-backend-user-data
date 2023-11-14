#!/usr/bin/env python3
"""
class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class authentication
    """
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ Require method authentication
        """
        if path and excluded_paths:
            if path in excluded_paths:
                return False
            if path[:-1] in excluded_paths or\
                    path + '/' in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ check header authorization
        """
        if request and request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ check current user
        """
        return None
