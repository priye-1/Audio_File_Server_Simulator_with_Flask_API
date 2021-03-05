''' This module defines the base class for unittests that will be inherited by other child classes'''

import os, sys
import unittest

sys.path.append(os.path.abspath('../music_api'))
import app as flask_app

sys.path.append(os.path.abspath('../music_api'))
import database.db as flask_db


class BaseCase(unittest.TestCase):
    '''
    Parent class to define base test methods 
    
    '''

    def setUp(self):
        ''' Function to set up test infrastructure before running test '''

        self.app = flask_app.app.test_client()
        self.db = flask_db.db.get_db()   # database instance


    def tearDown(self):
        '''Function to delete Database collections after the test is complete'''

        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)