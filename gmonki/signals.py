# -*- coding: utf-8 -*-
from gmonki import app
from flask.ext.user.signals import user_confirmed_email, user_changed_username
from gmonki import dbservice
from py2neo import neo4j

# common function to create/merge neo4j node corresponding to user id
def gdb_user_upsert(user_id):
	# create or merge cypher query template
	upsert_query_template = ('merge (p:person {gmonki_id:%d}) '
								'on create set p.created=timestamp() '
								'on match set p.accessed=timestamp() '
								'return p')
	# attempt to create user node
	try:
		dbservice.get_graph_db()
		new_node_query = neo4j.CypherQuery(app.gdb_client, (upsert_query_template % (user_id)))
		app.logger.info('cypher qs: ' + str(new_node_query.string))
		user_node_result = new_node_query.execute()
		app.logger.info('gdb_user_upsert SUCCESS User ID: ' + str(user_id) + " " + str(user_node_result[0]))
		return user_node_result
	except Exception, e:
		app.logger.error('gdb_user_upsert failed for User ID: ' + str(user_id) + str(e.__class__))
		return None

@user_confirmed_email.connect_via(app)
def user_confirmed_email_action(sender, user, **extra):
	# create new unique graph db node matching flask-user id
	try:
		result = gdb_user_upsert(user.id)	
		sender.logger.info('user_confirmed_email_action: ' + str(result[0]))
	except:
		sender.logger.error('user_confirmed_email_action: ERROR get_graph_db()')

@user_changed_username.connect_via(app)
def user_changed_name_action(sender, user, **extra):
	# create new unique graph db node matching flask-user id
	try:
		result = gdb_user_upsert(user.id)	
		sender.logger.info('user_changed_name_action: ' + str(result[0]))
	except:
		sender.logger.error('user_changed_name_action: ERROR get_graph_db()')
