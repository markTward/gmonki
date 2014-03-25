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
    return render_template('people/people.html', title='People')

@app.route('/people/invite')
@login_required
def invite_page():
    return render_template('people/invite.html', title='Invite')

@app.route('/people/connect')
@login_required
def connect_page():
    return render_template('people/connect.html', title='Connect')

@app.route('/places')
@login_required
def places_page():
    return render_template('places/places.html', title='Places')

@app.route('/places/locations')
@login_required
def locations_page():
    return render_template('places/locations.html', title='Locations')

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

@app.route('/member')
@login_required
def member_page():
    return render_template('member/member.html', title='Member')

@app.route('/member/profile')
@login_required
def profile_page():
    return render_template('member/profile.html', title='Profile -- ' + current_user.username)
