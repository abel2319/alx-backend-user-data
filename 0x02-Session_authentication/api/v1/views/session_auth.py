#!/usr/bin/env python3
""" Module of Users views
"""
from os import getenv
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login(request):
    """login user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == '':
        return jsonify({"error": "email missing"}), 400

    if not password and password == '':
        return jsonify({"error": "password missing"}), 400

    user = User.search(email)
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.get(id))
    res = jsonify(user.to_json())
    SESSION_NAME = getenv('SESSION_NAME')
    res.set_cookie(SESSION_NAME, session_id)
    return res
