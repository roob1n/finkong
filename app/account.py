from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from app.auth import login_required
from app.db import get_db

bp = Blueprint('account', __name__, url_prefix='/accounts')

@bp.route('/')
def index():
    db = get_db()
    accounts = db.execute(
        'SELECT a.id, a.title,'
        ' ROUND(SUM(CASE WHEN strftime("%Y-%m", p.created_at) = strftime("%Y-%m", "now", "-1 month") THEN p.amount_rappen ELSE 0 END) / 100.0, 2) AS total_last_month,'
        ' ROUND(SUM(CASE WHEN strftime("%Y-%m", p.created_at) = strftime("%Y-%m", "now") THEN p.amount_rappen ELSE 0 END) / 100.0, 2) AS total_current_month'
        ' FROM account AS a'
        ' LEFT JOIN position AS p ON a.id = p.account_id'
        ' GROUP BY a.id, a.title'
    ).fetchall()

    return render_template('account/index.html', accounts = accounts)

@bp.route('/view')
def view():
    return 'View Account'