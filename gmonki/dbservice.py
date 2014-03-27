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
	if not hasattr(app, 'gdb_client'):
		app.logger.info('get_graph_db(): try to ESTABLISH neo4j connection')
		try:
			gdb_url = app.config['GRAPHENEDB_URL']			
			service_root = neo4j.ServiceRoot(URI(gdb_url).resolve('/'))
			app.gdb_client = service_root.graph_db
			app.logger.info('neo4j: ' + str(service_root.graph_db))
			return app.gdb_client
		except:
			app.logger.error('neo4j: problems acquring graph db')
	else:
		app.logger.info('get_graph_db(): neo4j connection EXISTS')

