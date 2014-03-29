# -*- coding: utf-8 -*-
from gmonki import app
from flask.ext.user.signals import user_confirmed_email, user_changed_username
from gmonki import dbservice
from py2neo import neo4j

@user_confirmed_email.connect_via(app)
def user_confirmed_email_action(sender, user, **extra):
	
	# neo4j cypher query to create or merge into existing node based on fuid and username
	cypher_query_template = 'merge (p:person {username:"%s", fuid:%d}) return p'

	# create new unique graph db node with flask-user id and username
	try:
		dbservice.get_graph_db()
		new_node_query = neo4j.CypherQuery(app.gdb_client, (cypher_query_template % (user.username, user.id)))
		new_node_result = new_node_query.execute() 
		sender.logger.info('user_confirmed_email: ' + str(new_node_result[0]))
	except:
		sender.logger.error('create_gmonki_graph_user: ERROR get_graph_db()')

@user_changed_username.connect_via(app)
def user_changed_name_action(sender, user, **extra):
	
	# synch username between flask-user and  graph db
	try:
		dbservice.get_graph_db()
		gdb_user, = app.gdb_client.find('person',property_key='fuid', property_value=user.id)
		gdb_user['username'] = user.username
		sender.logger.info('SIGNAL user_changed_name: ' + str(gdb_user))
	except:
		sender.logger.error('create_gmonki_graph_user: ERROR get_graph_db()')
