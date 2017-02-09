# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

from app.model import Base


class Grant(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer, ForeignKey('user.user_id', ondelete='CASCADE')
    )
    user = relationship('User')

    client_id = Column(
        String(40), ForeignKey('client.client_id', ondelete='CASCADE'),
        nullable=False,
    )
    client = relationship('Client')
    code = Column(String(255), index=True, nullable=False)

    redirect_uri = Column(String(255))
    scope = Column(Text)
    expires = Column(DateTime)

    def delete(self, session):
        session.delete(self)
        session.commit()
        return self

    @property
    def scopes(self):
        if self.scope:
            return self.scope.split()
        return None
