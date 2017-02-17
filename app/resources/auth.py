# -*- coding: utf-8 -*-

import falcon
from app.resources.base import BaseResource
import requests
from app import errors


def validate_query_str(req, resp, resource, params):
    if not req.query_string:
        msg = 'You must pass some parameters through query string'
        raise falcon.HTTPBadRequest('Bad request', msg)


def parse_query_str(q_string):
    if q_string:
        separated_string = q_string.split('&')
        dict_params = {}

        for params in separated_string:
            key, value = params.split('=')
            dict_params[key] = value
        else:
            return dict_params

    return False


class AuthorizeResource(BaseResource):
    @falcon.before(validate_query_str)
    def on_get(self, req, res):
        dict_params = parse_query_str(req.query_string)
        print(dict_params)

        if 'redirect_uri' in dict_params:
            res.status = falcon.HTTP_301
            res.set_header('Location', dict_params['redirect_uri'] + '?code=123')
            self.on_success(res, [])
