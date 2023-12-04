from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
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