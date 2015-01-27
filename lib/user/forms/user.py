# coding: utf-8

from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Required, Optional, Email

class UserForm(Form):
    email = StringField(u"Email", [
        Required(u"El email es obligatorio"),
        Email(u"El email no es correcto")])
    password = PasswordField(u"Contraseña", [Optional()])
    active = BooleanField(u"¿Activo?", default=True)