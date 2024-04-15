# Welcome to Raspberry Pi workshop

I hope everyone learnt how to setup a Raspberry Pi and run Nginx server on it.
Now we will be building a simple API using Flask.

Please copy the code below and save it with `<your_name>.py` inside `src/routes` folder.
For example, if your name is bharath, then name of the file should be `bharath.py`.

Here is the code:
```python
from flask_restful import Resource

class Route(Resource):
	def get(self):
		return 'Hello, World!'
```

Replace the 'Hello, World!' with whatever you want.

[Click here for detailed explanation](https://scribehow.com/shared/Adding_your_own_endpoint_for_the_workshop__gUkmt_zsSyakKU-pqajSSA)

