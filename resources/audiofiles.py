''' This module defines methods for all endpoints'''

from flask import Blueprint, Response, request
from flask_restful import Resource
from database.models import Song, Podcast, AudioBook

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, InvalidQueryError

from resources.errors import SchemaValidationError, AudioFileAlreadyExistsError, \
InternalServerError, UpdatingAudioFileError, DeletingAudioFileError, AudioFileNotExistsError



#sample metadata
song = {}
podcast = {}
audio_book = {}

# create blueprint to structure application
audiofiles= Blueprint('audiofiles)', __name__)


file_types= {'song':Song, 'podcast': Podcast, 'audiobook': AudioBook }


class AudioFilesApi(Resource):
    '''
    Class to create and get audio files.  Handle get and post requests
    '''
    def get(self, audiofile):
        '''
            Function to retrieve all documents stored in a specified audiofile

            params:
                - audiofile: makes reference to an audio file type
                type: str
            
            returns:
                - json object
                - status
            
        '''
        try:
            file = file_types[audiofile].objects().to_json()
            return Response(file, mimetype="application/json", status=200)
        except Exception as e:
            raise InternalServerError


    def post(self, audiofile):
        '''
            Function to create a new document for a specified audio type

            params:
                - audiofile: makes reference to an audio file type
                type: str
            
            returns:
                - json object
                - status
            
        '''
        try:
            body = request.get_json()                   # receive json to be sent to database
            file = file_types[audiofile](**body).save() # saves in database
            id = file.id
            return{'id':str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise AudioFileAlreadyExistsError
        except Exception as e:
            raise InternalServerError



class ModifyAudioFileApi(Resource):
    '''
    Class to Modify or delete an audio file
    '''
    def put(self, audiofile, id):
        '''
            Function to modify a particular audiofile using its id 

            params:
                - audiofile: makes reference to an audio file type
                    type: str
                - id : specifies the id of the audiofile to be modified
                    type: int
            
            returns:
                - audiofile id
                - status
            
        '''
        try:
            body = request.get_json()                                     # receives the json to be updated with
            file_types[audiofile].objects.get(id=id).update(**body)       # updates data in database
            return f'{audiofile} with id: {id} has been updated', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingAudioFileError
        except Exception:
            raise InternalServerError  



    def delete(self, audiofile, id):
        '''
            Function to delete a particular audiofile using its id 

            params:
                - audiofile: makes reference to an audio file type
                    type: str
                - id : specifies the id of the audiofile to be modified
                    type: int
            
            returns:
                - audiofile id
                - status
            
        '''
        try:
            file = file_types[audiofile].objects.get(id=id).delete()              #deletes audiofile from database
            return f'{audiofile} with id: {id} has been updated', 200
        except DoesNotExist:
            raise DeletingAudioFileError
        except Exception:
            raise InternalServerError


class AudioFileApi(Resource):
    ''' Class  to retrieve a particular  audio  file '''
    def get(self, audiofile, id):
        '''
            Function to retrieve a particular audiofile using its id 

            params:
                - audiofile: makes reference to an audio file type
                    type: str
                - id : specifies the id of the audiofile to be modified
                    type: int
            
            returns:
                - json object
                - status
            
        '''
        
        try:
            file = file_types[audiofile].objects.get(id=id).to_json()
            return Response(file, mimetype="application/json", status=200)
        except DoesNotExist:
           raise AudioFileNotExistsError
        except Exception:
            raise InternalServerError
