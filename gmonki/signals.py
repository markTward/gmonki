# -*- coding: utf-8 -*-
from gmonki import app
from flask.ext.user.signals import user_confirmed_email, user_changed_username
from gmonki import dbservice
from py2neo import node

@user_confirmed_email.connect_via(app)
def user_confirmed_email_action(sender, user, **extra):
	sender.logger.info('SIGNAL user_confirmed_email: ' + str(user.id) + ' ' + str(user.username))
	
	# create new unique graph db node with flask-user id and username
	try:
		dbservice.get_graph_db()
		gdb_user = app.gdb_client.get_or_create_indexed_node('fuid', 'fuid', user.id, {'fuid':user.id, 'username':user.username})
		gdb_user.add_labels('entity', 'person')
	except:
		sender.logger.error('create_gmonki_graph_user: ERROR get_graph_db()')

@user_changed_username.connect_via(app)
def user_changed_name_action(sender, user, **extra):
	sender.logger.info('SIGNAL user_changed_name: ' + str(user.id) + ' ' + str(user.username))
	
	# synch username between flask-user and  graph db
	try:
		dbservice.get_graph_db()
		gdb_user, = app.gdb_client.find('person',property_key='fuid', property_value=user.id)
		gdb_user['username'] = user.username
	except:
		sender.logger.error('create_gmonki_graph_user: ERROR get_graph_db()')
