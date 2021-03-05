''' This module defines the database tables and fields '''
from .db import db
import datetime

class Song(db.Document):
    '''
    Class to create the Song table and its fields.

    class attributes:
        - id
        -  name
        - duration
        - uploaded_time
    
    '''
    id = db.IntField(required=True, primary_key=True)
    name = db.StringField(max_length=100, required=True) 
    duration = db.IntField(required=True) 
    uplopaded_time = db.DateTimeField(default=datetime.datetime.utcnow, required=True) 


class Podcast(db.Document):
    '''
    Class to create the Podcast table and its fields.

    class attributes:
        - id
        - name
        - duration
        - uploaded_time
        - host
        - participants
    
    '''
    id = db.IntField(required=True, primary_key=True) 
    name =  db.StringField(required=True, max_length=100)
    duration = db.IntField(required=True) 
    uploaded_time = db.DateTimeField(required=True, default=datetime.datetime.utcnow) 
    host = db.StringField(required=True, max_length=100) 
    participants = db.ListField(db.StringField(max_length=100), required=False, max_length=10)


class AudioBook(db.Document):
    '''
    Class to create the AudioBook table and its fields.

    class attributes:
        - id
        - title
        - author
        - narrator
        - duration_time
        - uploaded_time
    
    '''
    id = db.IntField(required=True, primary_key=True) 
    title = db.StringField(required=True, max_length=100) 
    author = db.StringField(required=True, max_length=100) 
    narrator = db.StringField(required=True, max_length=100) 
    duration_time = db.IntField(required=True) 
    uplopaded_time = db.DateTimeField(required=True, default=datetime.datetime.utcnow)
