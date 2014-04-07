# -*- coding: utf-8 -*-
"""
	things.py
"""

from flask import render_template
from flask.ext.user import login_required, current_user
from gmonki import app

@app.route('/things')
@login_required
def things_page():
	return render_template('things/things.html', title='Things')

@app.route('/things/capture')
@login_required
def capture_page():
	return render_template('things/capture.html', title='Capture')

@app.route('/things/catalog')
@login_required
def catalog_page():
	return render_template('things/catalog.html', title='Catalog')
