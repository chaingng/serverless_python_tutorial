from flask_blog.models.users import User
import os


def setup_auth(app, login_manager):
    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)


def is_production():
    return os.environ.get('SERVERLESS_BLOG_CONFIG') == 'production'
