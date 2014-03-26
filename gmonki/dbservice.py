# -*- coding: utf-8 -*-
"""
	dbservice.py
	application-wide database services
"""
import os
from gmonki import app
from py2neo import neo4j
from py2neo.packages.urimagic import URI

def get_graph_db():
	app.logger.info('get_graph_db(): attempt to establish neo4j connection')
	if not hasattr(app, 'gdb_client'):
		try:
			gdb_url = app.config['GRAPHENEDB_URL']			
			service_root = neo4j.ServiceRoot(URI(gdb_url).resolve('/'))
			app.logger.info('neo4j: ' + str(service_root.graph_db))
			return service_root.graph_db
		except:
			app.logger.error('neo4j: problems acquring graph db')

