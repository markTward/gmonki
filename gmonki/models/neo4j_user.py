class Neo4jGenericNode(object):
	def __init__(self, **initial_data):
		for key in initial_data:
			setattr(self, key, initial_data[key])

class GraphPerson(Neo4jGenericNode):
	pass

class GraphLocation(Neo4jGenericNode):
	pass

class GraphThing(Neo4jGenericNode):
	pass
