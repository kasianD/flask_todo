import functools

from flask import (
    Blueprint, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from app.forms import UserForm
from app.models import User


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/', methods=['GET', 'POST'])
def login():
    form = UserForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and not check_password_hash(user.password, form.password.data):
            return render_template('login.html', form=form, is_not_unique=True)

        if not user:
            user = User(
                username=form.username.data, 
                password=generate_password_hash(form.password.data)
            ).create()

        session['username'] = user.username
        session['user_id'] = user.id
        # print(form.username.data)
        # print(form.password.data)
        return redirect(url_for('index'))


    return render_template('login.html', form=form)


@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view





