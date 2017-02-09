# -*- coding: utf-8 -*-

import falcon

from app.resources.base import BaseResource
from app.model import Client
from app import errors


class ClientsResource(BaseResource):
    def on_get(self, req, res):
        session = req.context['session']
        client_dbs = session.query(Client).all()

        if client_dbs:
            obj = [client.to_dict() for client in client_dbs]
            self.on_success(res, obj)
        else:
            raise errors.AppError()