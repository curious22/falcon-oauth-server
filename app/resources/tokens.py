# -*- coding: utf-8 -*-

from app.resources.base import BaseResource
from app.model import Token
from app import errors


class TokenDisplayResource(BaseResource):
    def on_get(self, req, res):
        session = req.context['session']
        tokens = session.query(Token).all()

        if tokens:
            obj = [token.to_dict() for token in tokens]
            self.on_success(res, obj)
        else:
            raise errors.AppError()