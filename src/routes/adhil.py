from flask_restful import Resource

class Route(Resource):
	def get(self):
		return 'Hello, World!'
