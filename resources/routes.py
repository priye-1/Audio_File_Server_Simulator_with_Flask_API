''' This module is register endpoints '''

from .audiofiles import AudioFilesApi, ModifyAudioFileApi, AudioFileApi

# To register endpoints
def initialize_routes(api):
    api.add_resource(AudioFilesApi, '/api/<audiofile>')
    api.add_resource(ModifyAudioFileApi, '/api/<audiofile>/<id>')
    api.add_resource(AudioFileApi, '/api/<audiofile>/<id>')