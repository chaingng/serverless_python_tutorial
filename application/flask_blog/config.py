import os

class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = 'secret key'
    USERNAME = 'john'
    PASSWORD = 'due123'

class ProductionConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SERVERLESS_SECRET_KEY')
    USERNAME = 'john'
    PASSWORD = os.environ.get('SERVERLESS_USER_PW')
