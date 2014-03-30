# -*- coding: utf-8 -*-
"""
	member.py
"""

from flask import current_app, flash, redirect, render_template, request, url_for
from flask.ext.user import login_required, current_user
from gmonki import app, dbservice, forms

@app.route('/people')
@login_required
def people_page():
	return render_template('people/people.html', title='People')

@app.route('/people/profile', methods=['GET','POST'])
@login_required
def people_profile_page():
	# acquire graph db user info 
	dbservice.get_graph_db()
	gdb_user, = app.gdb_client.find('person',property_key='fuid', property_value=current_user.id)

	# initialize form
	form = forms.PeopleProfileForm(request.form)

	if request.method == 'POST':
		app.logger.debug('post-validate ')
		form.validate()
		app.logger.debug('form errors:' + str(form.errors))
		gdb_user['fullname'] = form.fullname.data
		gdb_user['address_default'] = form.address_default.data
		gdb_user['friend_sharing_default'] = form.friend_sharing_default.data
		gdb_user['neighborhood_sharing_default'] = form.neighborhood_sharing_default.data
		flash('GMonki Profile Updated', 'success')
		return redirect(form.next.data)
	else:
		app.logger.debug('form INITIALIZATION: ')
		form.fullname.data = gdb_user['fullname'] if 'fullname' in gdb_user else None
		form.address_default.data = gdb_user['address_default'] if 'address_default'in gdb_user else None
		form.friend_sharing_default.data = gdb_user['friend_sharing_default'] if 'friend_sharing_default' in gdb_user else 'friends'
		form.neighborhood_sharing_default.data = gdb_user['neighborhood_sharing_default'] if 'neighborhood_sharing_default' in gdb_user else False
		form.next.data = request.args.get('next',url_for('people_profile_page'))

	return render_template('people/people_profile.html', title='Profile', gdb_user=gdb_user, form=form)

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
def member_profile_page():
	return render_template('member/member_profile.html', title='Profile -- ' + current_user.username)

@app.route('/member/settings')
@login_required
def member_settings_page():
	return render_template('member/member_settings.html', title='Settings')
