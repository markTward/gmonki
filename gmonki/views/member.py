# -*- coding: utf-8 -*-
"""
	member.py
"""

from flask import render_template
from gmonki import app
from flask.ext.user import login_required, roles_required, current_user

@app.route('/people')
@login_required
def people_page():
    return render_template('people.html', title='People')

@app.route('/places')
@login_required
def places_page():
    return render_template('places.html', title='Places')

@app.route('/things')
@login_required
def things_page():
    return render_template('things.html', title='Things')

@app.route('/profile')
@login_required
def profile_page():
    return render_template('profile.html', title='Profile -- ' + current_user.username)
