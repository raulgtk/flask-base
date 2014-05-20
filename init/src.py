# coding: utf-8

import os
import importlib

def setup_packages(app):
    packages = app.config['LIBS']
    for package in packages:
        module = importlib.import_module('lib.%s' % package)
        app.register_blueprint(module.bp)

def setup_main(app):
    module = importlib.import_module('web')
    app.register_blueprint(module.bp)