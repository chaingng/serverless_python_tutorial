from flask_blog import db
from datetime import datetime

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, MapAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute

class Entry(Model):
    class Meta:
        table_name = "serverless_blog_entries"
        region = 'ap-northeast-1'
        host = "http://localhost:8000"
    id = NumberAttribute(hash_key=True, default=int(datetime.now().timestamp()))
    title = UnicodeAttribute(null=True)
    text = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute(default=datetime.now)
