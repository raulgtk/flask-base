# conding: utf-8

from flask import Blueprint

bp = Blueprint('web.layout', __name__, template_folder='templates', static_folder='static')