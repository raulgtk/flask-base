# coding: utf-8

from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Required, Optional

class UserForm(Form):
    email = StringField(u"Email", [Required(u"El email es obligatorio")])
    password = PasswordField(u"Contraseña", [Optional()])
    active = BooleanField(u"¿Activo?", default=True)