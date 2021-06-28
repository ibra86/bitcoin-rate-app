from flask import url_for, request, flash
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect

from app import app
from app.utils import get_user_from_storage, put_user_to_storage


@app.route('/user/create', methods=['POST'])
def user_create():
    email = request.json.get('email')
    password = request.json.get('password')
    password_hsh = generate_password_hash(password, method='sha256')

    user = get_user_from_storage(email)
    if user:
        return f'user {email} already exists'

    put_user_to_storage(email, password_hsh)

    return f'user {email} created'


@app.route('/user/login', methods=['POST'])
def user_login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = get_user_from_storage(email)
    if not user or not check_password_hash(user.password_hsh, password):
        return 'incorrect login'

    login_user(user)
    return f'user {email} logged in'
