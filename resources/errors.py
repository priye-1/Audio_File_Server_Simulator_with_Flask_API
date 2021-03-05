''' Module to create exception classes and handle errors'''

class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class AudioFileAlreadyExistsError(Exception):
    pass

class UpdatingAudioFileError(Exception):
    pass

class DeletingAudioFileError(Exception):
    pass

class AudioFileNotExistsError(Exception):
    pass


# define error messages and status
errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "UpdatingAudioFileError": {
         "message": "AudioFile does not exist",
         "status": 400
     },
     "AudioFileAlreadyExistsError": {
         "message": "AudioFile with given id already exists",
         "status": 400
     },
     "DeletingAudioFileError": {
         "message": "Audiofile does not exist",
         "status": 403
     },
     "AudioFileNotExistsError": {
         "message": "AudioFile does not exists",
         "status": 400
     },
}