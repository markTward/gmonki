# -*- coding: utf-8 -*-
"""
	places.py
"""

from flask import render_template
from flask.ext.user import login_required, current_user
from gmonki import app

@app.route('/places')
@login_required
def places_page():
	return render_template('places/places.html', title='Places')

@app.route('/places/locations')
@login_required
def locations_page():
	return render_template('places/locations.html', title='Locations')
