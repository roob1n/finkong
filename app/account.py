from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from app.auth import login_required
from app.db import get_db

bp = Blueprint('account', __name__, url_prefix='/accounts')

@bp.route('/')
@login_required
def index():
    db = get_db()
    accounts = db.execute(
        'SELECT a.id, a.title,'
        ' ROUND(SUM(CASE WHEN strftime("%Y-%m", p.created_at) = strftime("%Y-%m", "now", "-1 month") THEN p.amount_rappen ELSE 0 END) / 100.0, 2) AS total_last_month,'
        ' ROUND(SUM(CASE WHEN strftime("%Y-%m", p.created_at) = strftime("%Y-%m", "now") THEN p.amount_rappen ELSE 0 END) / 100.0, 2) AS total_current_month'
        ' FROM account AS a'
        ' LEFT JOIN position AS p ON a.id = p.account_id'
        ' WHERE a.user_id = ?'
        ' GROUP BY a.id, a.title', (g.user['id'],)
    ).fetchall()

    return render_template('account/index.html', accounts = accounts)

@bp.route('/<int:id>')
@login_required
def single(id):
    db = get_db()
    account = db.execute('SELECT * FROM account WHERE id = ?', (id,)).fetchone()

    # Check if the requested accounts belongs to the logged in user
    if(account['user_id'] != g.user['id']):
        abort(403, 'You have no access to this account.')

    positions = db.execute(
        'SELECT p.id, p.text, p.created_at, p.amount_rappen AS amount, p.category_id, c.title AS category'
        ' FROM position p'
        ' JOIN category c ON p.category_id = c.id'
        ' WHERE p.account_id = ?'
        ' ORDER BY p.created_at DESC;', (account['id'],)).fetchall()

    return render_template('account/single.html', account = account, positions = positions)