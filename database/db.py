''' This module is to integrate an instance of the ap with mongodb using mongoengine'''
from flask_mongoengine import MongoEngine

# initialize mongoengine to interact with  mongodb
db = MongoEngine()

def initialize_db(app):
    db.init_app(app)