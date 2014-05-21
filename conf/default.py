# coding: utf-8

import os

SITENAME = "flask-base"

# project dir
PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Secret key
# Use ``os.urandom(24)`` to generate a new one
SECRET_KEY = '\x8d\x98He\x07\x1f\x00\x8e\x90\xd2\xc5;\xe7\xebD\x1e\xebf,\x02F\x1b\xdc6'

# Paths & URLs
STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

# Debugging
DEBUG = True

# Database
DB_URI = 'sqlite:////tmp/test.db'

# Libraries to include
LIBS = [
    'dbtools',
    'user',
    'geo',
]