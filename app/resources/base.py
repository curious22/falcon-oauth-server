# -*- coding: utf-8 -*-

import falcon
import json
from datetime import timedelta
from falcon_oauth.provider.oauth2 import OAuthProvider
from falcon_oauth.utils import utcnow

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

from app import log
from app.utils.alchemy import new_alchemy_encoder
from app.errors import NotSupportedError
from app import model
from app.utils import auth as auth_utils

LOG = log.get_logger()


class BaseResource(object):
    HELLO_WORLD = {
        'message': 'Hello World'
    }

    def to_json(self, body_dict):
        return json.dumps(body_dict)

    def from_db_to_json(self, db):
        return json.dumps(db, cls=new_alchemy_encoder())

    def on_error(self, res, error=None):
        res.status = error['status']
        meta = OrderedDict()
        meta['code'] = error['code']
        meta['message'] = error['message']

        obj = OrderedDict()
        obj['meta'] = meta
        res.body = self.to_json(obj)

    def on_success(self, res, data=None):
        res.status = falcon.HTTP_200
        meta = OrderedDict()
        meta['code'] = 200
        meta['message'] = 'OK'

        obj = OrderedDict()
        obj['meta'] = meta
        obj['data'] = data
        res.body = self.to_json(obj)

    def on_get(self, req, res):
        if req.path == '/':
            res.status = falcon.HTTP_200
            res.body = self.to_json(self.HELLO_WORLD)
        else:
            raise NotSupportedError(method='GET', url=req.path)

    def on_post(self, req, res):
        raise NotSupportedError(method='POST', url=req.path)

    def on_put(self, req, res):
        raise NotSupportedError(method='PUT', url=req.path)

    def on_delete(self, req, res):
        raise NotSupportedError(method='DELETE', url=req.path)

auth = OAuthProvider()


@auth.clientgetter
def clientgetter(client_id, req):
    session = req.context['session']
    return session.query(model.Client).filter_by(client_id=client_id).first()


@auth.usergetter
def usergetter(username, password, req):
    session = req.context['session']

    user = session.query(model.User).filter_by(username=username).first()
    if user and auth_utils.verify_password(
            password,
            username.passwordencode('utf-8')
    ):
        return user
    return None


@auth.tokengetter
def tokengetter(req, access_token=None, refresh_token=None):
    session = req.context['session']

    if access_token:
        return session.query(model.Token).filter_by(
            access_token=access_token
        ).first()
    if refresh_token:
        return session.query(model.Token).filter_by(
            refresh_token=refresh_token
        ).first()

    return None


@auth.tokensetter
def tokensetter(metadata, req, *args, **kwargs):
    session = req.context['session']

    metadata['user_id'] = req.headers['X-User-Id']
    metadata['client_id'] = req.client_id

    token = model.Token(**metadata)
    session.add(token)
    session.commit()

    return token


@auth.grantgetter
def grantgetter(client_id, code, req):
    session = req.context['session']

    return session.query(model.Grant).filter_by(client_id=client_id, code=code)


@auth.grantsetter
def grantsetter(user_id, client_id, code, req, *args, **kwargs):
    session = req.context['session']

    expires = utcnow() + timedelta(seconds=100)
    grant = model.Grant(
        client_id=client_id,
        code=code,
        redirect_uri=req.context.get('redirect_uri'),
        scope=' '.join(req.context.get('scopes')),
        user_id=user_id,
        expires=expires,
    )

    session.add(grant)
    session.commit()
