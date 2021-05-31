from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from flask_blog.lib.utils import is_production
import os

class Session(Model):
    class Meta:
        table_name = "serverless_blog_sessions"
        region = 'ap-northeast-1'
        if is_production():
            aws_access_key_id = os.environ.get('SERVERLESS_AWS_ACCESS_KEY_ID')
            aws_secret_access_key = os.environ.get('SERVERLESS_AWS_SECRET_KEY')
        else:
            aws_access_key_id = 'AWS_ACEESS_KEY_ID'
            aws_secret_access_key = 'AWS_SECRET_ACCESS_KEY'
            host = "http://localhost:8000"
    SessionId = UnicodeAttribute(hash_key=True, null=False)
    Session = UnicodeAttribute(null=True)
