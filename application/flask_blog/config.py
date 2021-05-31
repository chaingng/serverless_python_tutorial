import os

class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = 'secret key'
    USERNAME = 'john'
    PASSWORD = 'due123'

    SESSION_TYPE = 'dynamodb'
    SESSION_DYNAMODB_TABLE = 'serverless_blog_sessions'
    SESSION_DYNAMODB_REGION = 'ap-northeast-1'
    SESSION_DYNAMODB_KEY_ID = 'AWS_ACEESS_KEY_ID'
    SESSION_DYNAMODB_SECRET = 'AWS_SECRET_ACCESS_KEY'
    SESSION_DYNAMODB_ENDPOINT_URL = 'http://localhost:8000'

class ProductionConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SERVERLESS_SECRET_KEY')
    USERNAME = 'john'
    PASSWORD = os.environ.get('SERVERLESS_USER_PW')

    SESSION_TYPE = 'dynamodb'
    SESSION_DYNAMODB_TABLE = 'serverless_blog_sessions'
    SESSION_DYNAMODB_REGION = 'ap-northeast-1'
    SESSION_DYNAMODB_KEY_ID = os.environ.get('SERVERLESS_AWS_ACCESS_KEY_ID')
    SESSION_DYNAMODB_SECRET = os.environ.get('SERVERLESS_AWS_SECRET_KEY')
    SESSION_DYNAMODB_ENDPOINT_URL = None