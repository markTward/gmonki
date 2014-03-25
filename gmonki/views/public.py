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
  return render_template('public/index.html', title='Home')

@app.route('/about')
def about_page():
    return render_template('public/about.html', title="About")

@app.route('/blog')
def blog_page():
    return render_template('public/blog.html', title="Blog")

@app.route('/contact')
def contact_page():
    return render_template('public/contact.html', title="Contact")

@app.route('/help')
def help_page():
    return render_template('public/help.html', title="Help")
