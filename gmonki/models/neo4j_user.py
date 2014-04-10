class Neo4jGenericNode(object):
	def __init__(self, **initial_data):
		for key in initial_data:
			setattr(self, key, initial_data[key])

class GraphPerson(Neo4jGenericNode):
	pass

class GraphAddress(Neo4jGenericNode):
	pass
