# -*- coding: utf-8 -*-
from gmonki import app
from flask.ext.user.signals import user_confirmed_email, user_changed_username, user_logged_in
from gmonki import dbservice
from py2neo import neo4j

@user_confirmed_email.connect_via(app)
def user_confirmed_email_action(sender, user, **extra):
	# create new unique graph db node matching flask-user id
	try:
		upsert_result = dbservice.gdb_user_upsert(user)	
		app.logger.info('user_confirmed_email_action SUCCESS User ID :: Name :: Node ==>' + 
							str(user.id) + " :: " + str(user.username)  + " :: " + str(upsert_result[0][0]._id))
	except:
		sender.logger.error('user_confirmed_email_action: ERROR get_graph_db()')

@user_changed_username.connect_via(app)
def user_changed_name_action(sender, user, **extra):
	# create new unique graph db node matching flask-user id
	try:
		upsert_result = dbservice.gdb_user_upsert(user)	
		app.logger.info('user_changed_name_action SUCCESS User ID :: Name :: Node ==>' + 
							str(user.id) + " :: " + str(user.username)  + " :: " + str(upsert_result[0][0]._id))
	except:
		sender.logger.error('user_changed_name_action: ERROR get_graph_db()')

@user_logged_in.connect_via(app)
def user_logged_in_action(sender, user, **extra):
	# create new unique graph db node matching flask-user id
	try:
		upsert_result = dbservice.gdb_user_upsert(user)	
		app.logger.info('user_logged_in_action SUCCESS User ID :: Name :: Node ==>' + 
							str(user.id) + " :: " + str(user.username)  + " :: " + str(upsert_result[0][0]._id))
	except:
		sender.logger.error('user_logged_in_action: ERROR get_graph_db()')
