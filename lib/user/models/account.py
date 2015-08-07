# coding=utf-8

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from lib.dbtools import session
from lib.dbtools import Model
from lib.dbtools import ModelMixin

class Account(ModelMixin, Model):
    __tablename__ = 'accounts'

    type = Column(String(32))
    user = relationship('User', uselist=False, back_populates='account', cascade='all, delete-orphan')

    __mapper_args__ = {
        'polymorphic_on': 'type',
        'polymorphic_identity': 'account'
    }