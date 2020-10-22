from flask import Flask
from config import Config
from flask_restful import Api
from .routes import initialize_routes
from .parser_listings import run_parser
from app import globals

globals.initialize()

app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
initialize_routes(api)
run_parser()




