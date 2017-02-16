# -*- coding: utf-8 -*-

import falcon

from app import log
from app.middleware import JSONTranslator, DatabaseSessionManager
from app.database import db_session, init_session

from app.resources import base
from app.resources import users, clients, grants, tokens
from app.errors import AppError

LOG = log.get_logger()


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        LOG.info('API Server is starting')

        self.add_route('/', base.BaseResource())
        self.add_route('/v1/users', users.Collection())
        self.add_route('/v1/clients', clients.ClientsResource())
        self.add_route('/v1/display_grants', grants.GrantDisplayResource())
        self.add_route('/v1/display_tokens', tokens.TokenDisplayResource())

        self.add_error_handler(AppError, AppError.handle)

init_session()
middleware = [JSONTranslator(), DatabaseSessionManager(db_session)]
application = App(middleware=middleware)


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 5000, application)
    httpd.serve_forever()
