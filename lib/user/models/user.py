# coding=utf-8

import string
import random

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from lib.dbtools import session
from lib.dbtools import Model
from lib.dbtools import ModelMixin

def get_random_hash():
    LENGHT = 40
    return ''.join(random.choice(string.letters) for i in xrange(LENGHT))

class AnonymousUser(object):

    @property
    def is_authenticated(self):
        return False

class User(ModelMixin, Model):
    __tablename__ = 'users'

    session_id = Column(String(40), default=get_random_hash, unique=True, index=True)
    username = Column(String(50), nullable=False, default="")
    email = Column(String(256), nullable=False, unique=True)
    password_hash = Column(String(66))

    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account', back_populates='users')

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        if value:
            self.password_hash = generate_password_hash(unicode(value))

    @property
    def is_authenticated(self):
        return True

    @property
    def role(self):
        if self.account:
            return self.account.type
        else:
            return None

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get(cls, id=None, email=None, session_id=None):
        query = session.query(cls)
        if id:
            query = query.filter(cls.id == id)
        elif email:
            query = query.filter(cls.email == email)
        elif session_id:
            query = query.filter(cls.session_id == session_id)
        return query.one()

    def __repr__(self):
        return '<User %r>' % (self.email)