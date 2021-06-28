from flask import Flask
from flask_login import LoginManager

from .users import User
from .utils import get_users_all

app = Flask(__name__)
app.secret_key = 'secret-key-to-be-later-changed'
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(email):
    users_all = get_users_all()
    if email not in users_all:
        return
    user = User(**users_all[email])
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


from . import routes  # noqa
from . import auth  # noqa
