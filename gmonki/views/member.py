# -*- coding: utf-8 -*-
"""
	member.py
"""

from flask import current_app, flash, redirect, render_template, request, url_for
from flask.ext.user import login_required, current_user
from gmonki import app, dbservice, forms
from gmonki.models import neo4j_user

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

	# create wtform compatible with local object of graph db user
	local_gdb_user = neo4j_user.GraphPerson(**gdb_user.get_properties())

	# initialize form with request and graph user instance
	form = forms.PeopleProfileForm(request.form, obj=local_gdb_user)
	form.next.data = request.args.get('next',url_for('people_profile_page'))

	if request.method == 'POST' and form.validate():
		form.populate_obj(local_gdb_user)
		exclude_list = ['submit','next']
		local_gdb_user_filtered_properties = {k:v for k,v in local_gdb_user.__dict__.items() if k not in exclude_list}
		gdb_user.set_properties(local_gdb_user_filtered_properties)
		flash('GMonki Profile Updated', 'success')
		return redirect(form.next.data)
	return render_template('people/people_profile.html', title='Profile & Preferences :: ' + current_user.username, form=form)

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
