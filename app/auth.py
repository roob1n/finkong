import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

#================
#   REGISTER
#================
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        
        if error is None:
            try:
                cursor.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)',
                    (username, generate_password_hash(password))
                )
            
                user_id = cursor.lastrowid

                # create one account for the new user
                cursor.execute(
                    'INSERT INTO account (title, user_id) VALUES (?, ?)',
                    ("Kong Konto #1", user_id)
                )

                db.commit()
            except db.IntegrityError:
                error = f'User {username} is already registered.'
            else:
                return redirect(url_for('auth.login'))
            
        flash(error)
        
    return render_template('auth/register.html')

#================
#   LOGIN
#================
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
            
        flash(error)

    return render_template('auth/login.html')

# Helpper routine that helps to fetch the user, if logged in
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

# Create a decorator for views that require to be logged in
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

#================
#   LOGOUT
#================
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
