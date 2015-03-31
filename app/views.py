__author__ = 'Guna'

from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    destinations = [ #sample array of locations
        {
            'traveller': {'nickname': 'Pradeep'},
            'line1': '1000, Glenmoore way',
            'line2': 'Apt 101',
            'city': 'Sunnyvale',
            'zip': 94085
        },

        {
            'traveller': {'nickname': 'Sankar'},
            'line1': '2000 Wildwood Ave',
            'line2': 'Apt 201',
            'city': 'Sunnyvale',
            'zip': 94086
        },

        {
            'traveller': {'nickname': 'Saravanan'},
            'line1': '151, Calderon Ave',
            'line2': 'Apt 262',
            'city': 'Mountain View',
            'zip': 94041
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           destinations=destinations)

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))