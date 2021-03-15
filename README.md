# Audio_File_Server_Simulator_with_Flask_API
### This Flask App simulates the behavior of an audio file server by integrating MongoDB  
The Audio files can be of three different  types:  SONG, PODCAST, AUDIOBOOK. 

The program performs the following operations on an audiofiles by specifying its types
- Creates audiofile  -> Endpoint: /api/\<audiofiletype\>
- Updates audiofile  -> Endpoint: /api/\<audiofiletype\>/\<id\>
- Delete audiofile   -> Endpoint: /api/\<audiofiletype\>/\<id\>
- Read audiofile(s)  -> Endpoint: /api/\<audiofiletype\>/\<id\>  and  /api/\<audiofiletype\>


## File structure
- Database : This directory holds the model definitions and the database configurations
- Resources : This directory is responsible for the exception definitions, the routes configurations and the CRUD method definitions
- Test : This directory holds test definitions for the programme


## Getting started   
### Installation

- Clone repository

    ```bash
     git@github.com:priye-1/Audio_File_Server_Simulator_with_Flask_API.git
    ```

- Setup virtualenvironment with virtualenvwrapper

    ```bash
    python -m venv .venv
    ```

- Install requirements

    ```terminal
    # use dev or production requirments depending on location
    pip install -r > requirements.txt
    ```
### Installing Mongodb community service
- https://docs.mongodb.com/manual/administration/install-community/

### Testing endpoints
Download and install Postman to test endpoints
- https://web.postman.co/

## Running Scripts
- Start program

    ```terminal
    python app.py
    ```
 
