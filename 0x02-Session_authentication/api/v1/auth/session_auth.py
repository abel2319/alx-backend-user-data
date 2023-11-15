#!/usr/bin/env python3
"""1. Empty session
"""
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import List, TypeVar


class SessionAuth(Auth):
    """ Session authentication
    """
    pass
