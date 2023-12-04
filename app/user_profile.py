from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from app.auth import login_required
from app.db import get_db

bp = Blueprint('user_profile', __name__, url_prefix='/profile')

@bp.route('/')
def index():
    return render_template('user_profile/index.html', user = g.user)

@bp.route('/edit', methods=('GET', 'POST'))
def edit():
    if request.method == 'POST':
        street = request.form['street']
        street_nr = request.form['street_nr']
        zip = request.form['zip']
        city = request.form['city']
        db = get_db()
        
        db.execute('UPDATE user SET street = ?, street_nr = ?, zip = ?, city = ? WHERE id = ?', (street, street_nr, zip, city, g.user['id']))

        db.commit()

        flash('User has been updated')
        return redirect(url_for('user_profile.index')) 
    
    return render_template('user_profile/edit.html', user = g.user)                        