from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('flask_blog.config')

login_manager = LoginManager()
login_manager.init_app(app)

from flask_blog.lib.utils import setup_auth
setup_auth(app, login_manager)

from flask_blog.views import views, entries
