# -*- coding: utf-8 -*-
"""
	dbservice.py
	application-wide database services
"""
import os
from gmonki import app
from py2neo import neo4j

# establisth neo4j client and associated with the app
def get_graph_db():
	if not hasattr(app, 'gdb_client'):
		try:
			gdb_url = app.config['GRAPHENEDB_URL'] + '/db/data/'
			app.gdb_client = neo4j.GraphDatabaseService(gdb_url)
			app.logger.info('py2neo: SUCCESS ' + str(app.gdb_client.graph_db))
			return app.gdb_client
		except:
			app.logger.error('py2neo: ERROR problems acquring graph db')
	else:
		app.logger.info('get_graph_db(): neo4j connection EXISTS')

# common function to create/merge neo4j node corresponding to user id
def gdb_user_upsert(user):
    # create or merge cypher query template
    upsert_query_string = ('merge (p:person {{id:{uid}}}) '
                                'on create set p.username="{uname}", p.created=timestamp() '
                                'on match  set p.username="{uname}", p.accessed=timestamp() '
                                'return p').format(uid=user.id, uname=user.username)
    # attempt to create user node
    try:
        get_graph_db()
        upsert_query = neo4j.CypherQuery(app.gdb_client, upsert_query_string)
        app.logger.info('cypher qs: ' + str(upsert_query.string))
        upsert_result = upsert_query.execute()
        app.logger.info('gdb_user_upsert SUCCESS: ' + str(upsert_result[0]))
        return upsert_result
    except Exception, e:
        app.logger.error('gdb_user_upsert failed for User ID: ' + str(user.id) + str(e.__class__))
        return None

# common function to create/merge neo4j node corresponding to user id
def gdb_address_upsert(location):
    # create or merge cypher query template
    upsert_query_string = ('merge (a:address {{full_address:"{location_text}"}}) '
                                'on create set a.created=timestamp() '
                                'on match  set a.accessed=timestamp() '
                                'return a').format(location_text=location)
    # attempt to create user node
    try:
        get_graph_db()
        upsert_query = neo4j.CypherQuery(app.gdb_client, upsert_query_string)
        app.logger.info('cypher qs: ' + str(upsert_query.string))
        upsert_result = upsert_query.execute()
        app.logger.info('gdb_address_upsert SUCCESS: ' + str(upsert_result[0]))
        return upsert_result
    except Exception, e:
        app.logger.error('gdb_address_upsert failed for User ID: ' + str(location) + str(e.__class__))
        return None
