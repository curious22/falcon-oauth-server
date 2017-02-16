# -*- coding: utf-8 -*-

from app.resources.base import BaseResource
from app.model import Token
from app import errors


class GrantDisplayResource(BaseResource):
    def on_get(self, req, res):
        session = req.context['session']
        grants = session.query(Token).all()

        if grants:
            obj = [grant.to_dict() for grant in grants]
            self.on_success(res, obj)
        else:
            raise errors.AppError()
