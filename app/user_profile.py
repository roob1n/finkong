from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from app.auth import login_required
from app.db import get_db

bp = Blueprint('user_profile', __name__, url_prefix='/profile')

@bp.route('/')
def index():
    return render_template('user_profile/index.html', user = g.user)
