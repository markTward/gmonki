# -*- coding: utf-8 -*-
"""
	people.py
"""

from flask import current_app, flash, redirect, render_template, request, url_for
from flask.ext.user import login_required, current_user
from gmonki import app, dbservice, forms
from gmonki.models import neo4j_user
from py2neo import rel

@app.route('/people')
@login_required
def people_page():
	return render_template('people/people.html', title='People')

@app.route('/people/profile', methods=['GET','POST'])
@login_required
def people_profile_page():
	# acquire graph db user info 
	dbservice.get_graph_db()
	gdb_user, = app.gdb_client.find('person',property_key='id', property_value=current_user.id)

	# create wtform compatible with local object of graph db user
	local_gdb_user = neo4j_user.GraphPerson(**gdb_user.get_properties())

	# attempt to acquire primary address node
	gdb_primary_address_rel = list(app.gdb_client.match(start_node=gdb_user, rel_type="PRIMARY_ADDRESS"))
	if gdb_primary_address_rel:
		gdb_primary_address_node = gdb_primary_address_rel[0].end_node
		local_gdb_primary_address = neo4j_user.GraphAddress(**gdb_primary_address_node.get_properties())
	else:
		local_gdb_primary_address = neo4j_user.GraphAddress()
		local_gdb_primary_address.full_address = None

	# initialize form with request and graph user instance
	form = forms.PeopleProfileForm(request.form, obj=local_gdb_user, primary_address=local_gdb_primary_address.full_address)
	form.next.data = request.args.get('next',url_for('people_profile_page'))

	if request.method == 'POST' and form.validate():
		form.populate_obj(local_gdb_user)
		exclude_list = ['submit','next','primary_address']
		local_gdb_user_filtered_properties = {k:v for k,v in local_gdb_user.__dict__.items() if k not in exclude_list}
		gdb_user.set_properties(local_gdb_user_filtered_properties)
		if form.primary_address.data:
			if gdb_primary_address_rel:
				gdb_primary_address_node['full_address'] = form.primary_address.data
			else:
				pa, = dbservice.gdb_address_upsert(form.primary_address.data)
				pa_rel1 = app.gdb_client.create(rel(gdb_user,"PRIMARY_ADDRESS",pa[0]))
				pa_rel2 = app.gdb_client.create(rel(gdb_user,"ADDRESS",pa[0]))
				
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
