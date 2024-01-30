from functools import wraps

from flask_httpauth import HTTPTokenAuth
from flask import current_app as cdp_app
from config import BaseConfig

import app
from app.lib.jwt_token import JwtToken
from flask import jsonify, g
from http import HTTPStatus
from app.lib.constants import ADMIN_ROLE

token_auth = HTTPTokenAuth(scheme='bearer')


@token_auth.verify_token
def verify_token(token):
    # client_id = cdp_app.config.get('CLIENT_ID')
    # client_secret = cdp_app.config.get('CLIENT_SECRET')
    client_id = BaseConfig.CLIENT_ID
    client_secret= BaseConfig.CLIENT_SECRET
    print("CLINET ID IS::::::", client_id)
    print("CLIENT SECRET is:::::", client_secret)
    print("TOKEN VALUE IS:::::::::::::", token)
    jwt_payload = JwtToken.validate_token(token, client_id, client_secret)
    if not jwt_payload:
        print("INNNNNNNNNNNN FALSE")
        return False
    g.jwt_payload = jwt_payload
    g.token = token
    return True


@token_auth.error_handler
def auth_error_handler(status):
    return jsonify(
        {'status': 'error', 'message': 'Access Denied. Invalid Auth Token (or) Unauthorized Token'}
    ), status


def authorize_admin(api_method):
    @wraps(api_method)
    @token_auth.login_required
    def wrapper(*args, **kwargs):
        if ADMIN_ROLE not in g.jwt_payload.get('roles', []):
            return jsonify({'status': 'error', 'message': "Access rejected!, Access  restricted as you are not Admin"}
                           ), HTTPStatus.FORBIDDEN
        return api_method(*args, **kwargs)

    return wrapper


def authorize_role(role_name):
    def decorated(api_method):
        @wraps(api_method)
        @token_auth.login_required
        def wrapper(*args, **kwargs):
            if role_name not in g.jwt_payload.get('roles', []):
                return jsonify({'status': 'error', 'message': "Access rejected!, Access  restricted as you are not "
                                                              "Admin"}
                               ), HTTPStatus.FORBIDDEN
            return api_method(*args, **kwargs)
        return wrapper
    return decorated


# To verify whether the role has Read/Write access or not
def authorize_role_access(role_name, access):
    def decorated(api_method):
        @wraps(api_method)
        @token_auth.login_required
        def wrapper(*args, **kwargs):
            if role_name not in g.jwt_payload.get('roles', []):
                return jsonify({'status': 'error', 'message': "Access rejected!, Access  restricted as you are not "
                                                              "part of {role_name}"
                                }
                               ), HTTPStatus.FORBIDDEN
            return api_method(*args, **kwargs)
            if access not in g.jwt_payload.get('access', []):
                return jsonify(
                    {'status': 'error', 'message': 'Access restricted because you don\'t have {access} permission'})
            return api_method(*args, **kwargs)
        return wrapper

    return decorated
