# -*- coding: utf-8 -*-
"""
	member.py
"""

from flask import render_template
from flask.ext.user import login_required, current_user
from gmonki import app

@app.route('/member')
@login_required
def member_page():
	return render_template('member/member.html', title='Member')

@app.route('/member/profile')
@login_required
def member_profile_page():
	return render_template('member/member_profile.html', title='Profile -- ' + current_user.username)

@app.route('/member/settings')
@login_required
def member_settings_page():
	return render_template('member/member_settings.html', title='Settings')
