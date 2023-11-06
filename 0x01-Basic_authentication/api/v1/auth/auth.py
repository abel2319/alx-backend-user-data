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
        return False

    def authorization_header(self, request=None) -> str:
        """ check header authorization
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ check current user
        """
        return None
