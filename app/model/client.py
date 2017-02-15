# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String, Text

from app.model import Base


class Client(Base):
    name = Column(String(100), nullable=False)
    client_id = Column(String(40), primary_key=True)
    client_secret = Column(String(80), nullable=False, unique=True, index=True)
    _redirect_uris = Column(Text)
    default_scope = Column(Text, default='email address')

    def __repr__(self):
        return 'Client(name={}, client_id={}, client_secret={})'.format(
            self.name, self.client_id, self.client_secret
        )

    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        return self.redirect_uris[0]

    @property
    def default_scopes(self):
        if self.default_scope:
            return self.default_scope.split()
        return []

    @property
    def allowed_grant_types(self):
        return ['authorization_code', 'password', 'client_credentials',
                'refresh_token']

    FIELDS = {
        'name': str,
        'client_id': str,
        'default_scope': str
    }

    FIELDS.update(Base.FIELDS)