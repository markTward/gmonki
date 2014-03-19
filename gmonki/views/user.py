# -*- coding: utf-8 -*-
"""
	user.py
"""

from flask import render_template
from gmonki import app
from flask.ext.user import login_required, roles_required, current_user

@app.route('/profile')
@login_required
def profile_page():
    return render_template('profile.html', title='Profile -- ' + current_user.username)
