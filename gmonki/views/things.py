# -*- coding: utf-8 -*-
"""
	things.py
"""

from flask import render_template
from flask.ext.user import login_required, current_user
from gmonki import app, dbservice
from gmonki.models import neo4j_user

@app.route('/things')
@login_required
def things_page():
	dbservice.get_graph_db()
	gdb_user, = app.gdb_client.find('person',property_key='id', property_value=current_user.id)
	things = [neo4j_user.GraphThing(**t.end_node.get_properties()) for t in list(app.gdb_client.match(start_node=gdb_user, rel_type="OWNS"))]
	app.logger.debug('Things: ' + str(things))
	return render_template('things/things.html', title='Things', things=things)

@app.route('/things/capture')
@login_required
def capture_page():
	return render_template('things/capture.html', title='Capture')

@app.route('/things/catalog')
@login_required
def catalog_page():
	return render_template('things/catalog.html', title='Catalog')
