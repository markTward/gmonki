# -*- coding: utf-8 -*-
"""
	standard.py
"""

from flask import render_template
from gmonki import app
from flask.ext.user import login_required, roles_required

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', title='Home')

@app.route('/about')
def about_page():
    return render_template('about.html', title="About")

@app.route('/profile')
@login_required
def profile_page():
    return render_template('profile.html', title="Profile")
