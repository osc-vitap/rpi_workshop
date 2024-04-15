import os
import importlib
from flask_restful import Api

def load_routes(api: Api) -> None:
	print(os.getcwd())
	for route in os.listdir('./src/routes'):
		if not route.endswith('.py') \
			or route == '__init__.py':
			continue

		route = route.replace('.py', '')
		module_name = f'routes.{route}'
		module = importlib.import_module(module_name)

		print(f'Loading route: {route}')
		print(f'Route: {module.Route}')
		print(module_name)
		api.add_resource(module.Route, f'/{route}', endpoint=module_name)
