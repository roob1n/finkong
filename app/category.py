from flask import (Blueprint, flash, g, redirect, render_template, request, url_for, jsonify)
from app.auth import login_required
from app.db import get_db

bp = Blueprint('category', __name__, url_prefix='/category')

@bp.route('/')
@login_required
def index():
    db = get_db()
    categories = db.execute(
        'SELECT * FROM category'
    ).fetchall()

    return render_template('category/index.html', categories = categories)

@bp.route('/<int:id>')
@login_required
def single(id):
    db = get_db()

    category = db.execute('SELECT * FROM category WHERE id = ?', (id,)).fetchone()

    positions = db.execute(
            'SELECT p.id, p.text, p.created_at, ROUND(p.amount_rappen / 100.0, 2) AS amount, a.title AS account'
            ' FROM position p'
            ' JOIN account a ON p.account_id = a.id'
            ' WHERE p.category_id = ?'
            ' ORDER BY account, p.created_at DESC;', (category['id'],)).fetchall()
    
    grouped_positions = {}
    for position in positions:
        account = position['account']
        if account not in grouped_positions:
            grouped_positions[account] = []
        position_dict = dict(zip(('id', 'text', 'created_at', 'amount', 'account'), position))
        grouped_positions[account].append(position_dict)

    #return jsonify(grouped_positions)
    return render_template('category/single.html', category = category, account_data = grouped_positions)

