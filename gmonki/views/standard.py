# -*- coding: utf-8 -*-
"""
	standard.py
"""

from flask import render_template
from gmonki import app
from flask.ext.user import login_required, roles_required, current_user

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', title='Home')

@app.route('/about')
def about_page():
    return render_template('about.html', title="About")

@app.route('/blog')
def blog_page():
    return render_template('blog.html', title="Blog")
