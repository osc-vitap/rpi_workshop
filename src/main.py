from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from routes import load_routes
import os

load_dotenv(find_dotenv('../.env'))
app = Flask(__name__)
CORS(app)
api = Api(app)
load_routes(api)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get('APP_PORT')) or 5000
    )
