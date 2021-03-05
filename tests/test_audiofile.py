''' Module to create tests for various mehtods '''

import json
import unittest
import datetime
from BaseCase import BaseCase

audiofile = "song"
BASE_URL = f"api/{audiofile}"
BAD_URL = f"api/{audiofile}/"


class TestAudioFile(BaseCase):
    '''
    Class to create tests for methods and endpoints.  It inherits the base class 'BaseCase'

    '''

    def test_empty_response(self):

        ''' Method to test empty responses'''

        print("\n********************* Testing for empty response *********************")
        response = self.app.get(BASE_URL)
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)


    def test_audiofile_not_exist(self):

        ''' Method to test response for none existing audio files'''

        print("\n************************** Testing for none existing file using wrong url *********************")
        response = self.app.get(BAD_URL)
        self.assertEqual(response.status_code, 404)


    def test_get_one_audiofile(self):

        ''' Test get method for a defined audiofile '''

        print("\n************************** Testing To get one audio file*********************")

        # first create audiofile document
        audio_file_payload = {"id"  :789, "name" : "shade", "duration" : 6778}
        response = self.app.post(BASE_URL,
                headers={"Content-Type": "application/json"},
                data=json.dumps(audio_file_payload))

        # get recently created audiofile document 
        response2 = self.app.get(f"{BASE_URL}/{audio_file_payload['id']}")
        
        # get the name of document 
        data = response2.json['name']
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, 'shade')



    def test_create_audiofile(self):

        ''' Test to create an audiofile '''

        print("\n************************** Testing to create  an audiofile *********************")
        audio_file_payload = json.dumps({
            "id"  :789,
            "name" : "shade",
            "duration" : 6778
        })
        response = self.app.post(BASE_URL,
                headers={"Content-Type": "application/json"},
                data=audio_file_payload)

        #Test if 'id' returned is a string and if response is 200
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
    

    def test_update_audiofile(self):

        ''' Method to test empty responses '''

        print("\n************************** Testing to update  an audiofile *********************")

        # first create audiofile document
        audio_file_payload = {"id"  :789, "name" : "priye", "duration" : 6778}
        response = self.app.post(BASE_URL,
                headers={"Content-Type": "application/json"},
                data=json.dumps(audio_file_payload))

        self.assertEqual(response.status_code, 200)


        # make put request using the same id recently created
        modified_payload = {"id"  :789, "name" : "shade", "duration" : 3490}

        response2 = self.app.put(f"{BASE_URL}/{audio_file_payload['id']}",
                headers={"Content-Type": "application/json"},
                data=json.dumps(modified_payload))

        # get recently created audiofile document 
        response2 = self.app.get(f"{BASE_URL}/{audio_file_payload['id']}")
        
        # get the modified name of the document 
        data = response2.json['name']
        
        # test status codes and names changed is reflected
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, 'shade')


    def test_delete_audiofile(self):

        ''' Method to test deleted responses '''

        print("\n************************** Testing an audiofile delete *********************")

        # first create audiofile document
        audio_file_payload = {"id"  :789, "name" : "priye", "duration" : 6778}
        
        response = self.app.post(BASE_URL,
                headers={"Content-Type": "application/json"},
                data=json.dumps(audio_file_payload))

        # make request to delete 
        response2 = self.app.delete(f"{BASE_URL}/{audio_file_payload['id']}",
                headers={"Content-Type": "application/json"},
                data=json.dumps(audio_file_payload))
        
        self.assertEqual(response2.status_code, 200)
    



if __name__ == "__main__":
    unittest.main()
