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

    if(not account_belongs_to_user(id)):
        abort(403, 'You have no access to this account.')

    account = db.execute('SELECT * FROM account WHERE id = ?', (id,)).fetchone()

    positions = db.execute(
        'SELECT p.id, p.text, p.created_at, p.amount_rappen AS amount, p.category_id, c.title AS category, c.color AS category_color'
        ' FROM position p'
        ' JOIN category c ON p.category_id = c.id'
        ' WHERE p.account_id = ?'
        ' ORDER BY p.created_at DESC;', (account['id'],)).fetchall()

    return render_template('account/single.html', account = account, positions = positions)

# Add new position to account with id
@bp.route('/<int:id>/add', methods=('GET', 'POST'))
@login_required
def add(id):
    db = get_db()

    if request.method == 'POST':

        if(not account_belongs_to_user(id)):
            abort(403, 'You have no access to this account.')

        text = request.form['posting_text']
        amount = request.form['amount']
        category_id = request.form['category']
        
        db.execute('INSERT INTO position (text, account_id, amount_rappen, category_id) VALUES (?, ?, ?, ?)',
                        (text, id, amount, category_id))
        
        db.commit()
        
        return redirect(url_for('account.single', id = id))
    
    categories = db.execute('SELECT id, title FROM category;').fetchall();
    account = db.execute('SELECT * FROM account WHERE id = ?', (id,)).fetchone();
    
    return render_template('account/add.html', categories = categories, account = account, )
    
   
def account_belongs_to_user(id):
    db = get_db()
    account = db.execute('SELECT * FROM account WHERE id = ?', (id,)).fetchone()

    return account['user_id'] == g.user['id']