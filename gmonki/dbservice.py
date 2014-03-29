# -*- coding: utf-8 -*-
"""
	dbservice.py
	application-wide database services
"""
import os
from gmonki import app
from py2neo import neo4j

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

