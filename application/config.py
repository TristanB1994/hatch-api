import os
from flask import url_for, current_app

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base Config"""

    
class ProductionConfig(Config):
    """Production Config"""


class DevelopmentConfig(Config):
    """Dev Config"""

    WTF_CSRF_ENABLED = False
    CSRF_ENABLED = False

class TestingConfig(Config):
    """Testing Config"""

    TESTING = True
    WTF_CSRF_ENABLED = False
    CSRF_ENABLED = False

