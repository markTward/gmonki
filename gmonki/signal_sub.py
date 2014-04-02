# -*- coding: utf-8 -*-
from gmonki import app
from flask.ext.user.signals import user_confirmed_email, user_changed_username, user_logged_in
from gmonki import dbservice
from py2neo import neo4j

# common function to create/merge neo4j node corresponding to user id
def gdb_user_upsert(user):
	# create or merge cypher query template
	upsert_query_string = ('merge (p:person {{id:{uid}}}) '
								'on create set p.username="{uname}", p.created=timestamp() '
								'on match  set p.username="{uname}", p.accessed=timestamp() '
								'return p').format(uid=user.id, uname=user.username)
	# attempt to create user node
	try:
		dbservice.get_graph_db()
		upsert_query = neo4j.CypherQuery(app.gdb_client, upsert_query_string)
		app.logger.info('cypher qs: ' + str(upsert_query.string))
		upsert_result = upsert_query.execute()
		app.logger.info('gdb_user_upsert SUCCESS: ' + str(upsert_result[0]))
		return upsert_result
	except Exception, e:
		app.logger.error('gdb_user_upsert failed for User ID: ' + str(user.id) + str(e.__class__))
		return None

@user_confirmed_email.connect_via(app)
def user_confirmed_email_action(sender, user, **extra):
	# create new unique graph db node matching flask-user id
	try:
		upsert_result = gdb_user_upsert(user)	
		app.logger.info('user_confirmed_email_action SUCCESS User ID :: Name :: Node ==>' + 
							str(user.id) + " :: " + str(user.username)  + " :: " + str(upsert_result[0][0]._id))
	except:
		sender.logger.error('user_confirmed_email_action: ERROR get_graph_db()')

@user_changed_username.connect_via(app)
def user_changed_name_action(sender, user, **extra):
	# create new unique graph db node matching flask-user id
	try:
		upsert_result = gdb_user_upsert(user)	
		app.logger.info('user_changed_name_action SUCCESS User ID :: Name :: Node ==>' + 
							str(user.id) + " :: " + str(user.username)  + " :: " + str(upsert_result[0][0]._id))
	except:
		sender.logger.error('user_changed_name_action: ERROR get_graph_db()')

@user_logged_in.connect_via(app)
def user_logged_in_action(sender, user, **extra):
	# create new unique graph db node matching flask-user id
	try:
		upsert_result = gdb_user_upsert(user)	
		app.logger.info('user_logged_in_action SUCCESS User ID :: Name :: Node ==>' + 
							str(user.id) + " :: " + str(user.username)  + " :: " + str(upsert_result[0][0]._id))
	except:
		sender.logger.error('user_logged_in_action: ERROR get_graph_db()')
