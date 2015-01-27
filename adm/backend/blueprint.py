# conding: utf-8

from flask import Blueprint

bp = Blueprint('adm.backend', __name__, template_folder='templates', static_folder='static', url_prefix='/admin')