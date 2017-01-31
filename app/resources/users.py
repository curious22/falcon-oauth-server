# -*- coding: utf-8 -*-

import falcon

from cerberus import Validator, DocumentError

from app import log
from app.resources.base import BaseResource
from app.utils.auth import encrypt_token, hash_password, uuid
from app.model import User
from app.errors import AppError, InvalidParameterError

LOG = log.get_logger()


FIELDS = {
    'username': {
        'type': 'string',
        'required': True,
        'minlength': 4,
        'maxlength': 20
    },
    'email': {
        'type': 'string',
        'regex': '[a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}',
        'required': True,
        'maxlength': 320
    },
    'password': {
        'type': 'string',
        'regex': '[0-9a-zA-Z]\w{3,14}',
        'required': True,
        'minlength': 8,
        'maxlength': 64
    },
}


def validate_user_create(req, res, resource, params):
    schema = {
        'username': FIELDS['username'],
        'email': FIELDS['email'],
        'password': FIELDS['password'],
    }

    v = Validator(schema)
    try:
        if not v.validate(req.context['data']):
            raise InvalidParameterError(v.errors)
    except DocumentError:
        raise InvalidParameterError('Invalid Request %s' % req.context)


class Collection(BaseResource):
    """
    Handle for endpoint: /v1/users
    """
    @falcon.before(validate_user_create)
    def on_post(self, req, res):
        session = req.context['session']
        user_req = req.context['data']
        print(req.context['data'])
        if user_req:
            user = User()
            user.username = user_req['username']
            user.email = user_req['email']
            user.password = hash_password(user_req['password']).decode('utf-8')
            sid = uuid()
            user.sid = sid
            user.token = encrypt_token(sid).decode('utf-8')
            session.add(user)
            self.on_success(res, None)
        else:
            raise InvalidParameterError(req.context['data'])

    # @falcon.before(auth_required)
    def on_get(self, req, res):
        session = req.context['session']
        user_dbs = session.query(User).all()
        if user_dbs:
            obj = [user.to_dict() for user in user_dbs]
            self.on_success(res, obj)
        else:
            raise AppError()

    # @falcon.before(auth_required)
    def on_put(self, req, res):
        pass
