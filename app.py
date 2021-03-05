''' This module runs the entire program '''
from flask_restful import Api
from resources.errors import errors
from database.db import initialize_db
from flask import Flask, request, Response
from database.models import Song, Podcast, AudioBook
from resources.routes import initialize_routes


app = Flask(__name__)



# create instance of the API
api = Api(app, errors =errors)



# comment this section to run unittests
'''**************************************************'''

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/audio_files'
}
'''**************************************************'''




# remove comments from this section to run unittests
'''**************************************************'''

# MONGODB_SETTINGS = {
#     'host': 'mongodb://localhost/audio_files'
# }
'''**************************************************'''


# initialize databasee and routes
initialize_db(app)
initialize_routes(api)


# comment this section to run unittest
app.run(port=7000)