## These are routes for fastAPI. The discord bot API will send requests and file data to this local server and it will execute certain SQL
##  Instructions so as to either add a submission, return a submission, delete a submission or list all submissions.

##Currently, return submission and delete submission returns and deletes all submissions by the user_id.
##Needs to only return and delete one specific file from the user_id. This could perhaps be remedied by asking for more than
##The user_id. Perhaps a combination of user_id and file_name. Or perhaps just the id PRIMARY KEY in general.


## All routes are merely end-of-ticket stubs for the main URL which is http://127.0.0.1:8000
## This URL is currently a local host link because this has not been deployed.
## An example of how one of these routes can be used is the following. For the list_submissoins route
## The URL is http://127.0.0.1:8000/list_submissions

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlite_tutorial.database import get_connection, init_db
import sqlite3
from secret import CLIENT_ID, CLIENT_SECRET, CLIENT_URL
import requests
from fastapi.responses import RedirectResponse

init_db()

app = FastAPI()

class Submission(BaseModel):
    user_id: str = ""
    file_name: str = ""
    file_type: str = ""

## When routed to the home domain '/' It simply returns Hello World!
## UPDATE NEEDED:
##
##
@app.get("/")
def root():
    return ("Hello World")

## This is a post route. This decides what happens when you post to the /items endpoint. If the item is an Item
## meaning, if it has the variables text and is_done defined, it creates a new Item and appends it to the items list
## UPDATE NEEDED:
##     needs to insert into sqlite table
##     also needs to establish connection to table
##

@app.post("/submissions")
def insert_submission(submission: Submission):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(" INSERT INTO discord_files (user_id, file_name, file_type) VALUES (?, ?, ?)",
                            (submission.user_id, submission.file_name, submission.file_type))
    connection.commit()
    connection.close()
    return ("Inserted submission.")

## This is a get request route. It responds with an Item. The user needs simply to include an item_id and if the item_id
##is within the size of the list, returns the Item at that position.
## UPDATE NEEDED:
##      needs to select individual element from the sql table
##
@app.get('/submissions/{user_id}')
def get_submissions(user_id: str):
    connection = get_connection()
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM discord_files WHERE user_id LIKE ?" , (user_id,))
    printed_result = result.fetchall()
    connection.close()
    return(printed_result)
    
## This is a delete request route. Deletes the item at the item_ID position!!!
## UPDATE NEEDED:
##      needs to remove from table instead of removing from list
##
@app.delete('/submissions/{user_id}')
def delete_item(user_id:str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM discord_files WHERE user_id = ?", (user_id,))
    connection.commit()
    connection.close()
    return ("Item deleted!")

##Another gret request, this one does not require an item_id. And so, if one is not provided, returns the first 10 items in the list
## UPDATE NEEDED:
##    needs to select * from table and return that instead
##
##
@app.get('/list_submissions')
def list_submissions(submission_limit: int = 10):
    connection = get_connection()
    cursor = connection.cursor()
    cursor_printed = cursor.execute("SELECT * FROM discord_files LIMIT ? ", (submission_limit,)).fetchall()
    connection.close()
    return(cursor_printed)


## This is a route that is redirected to after the user logs in. 
## After this we get an authorization token.
## The plan now is to use this authorization token to get the user id and redirect the user there.
## There is no security so far with this type of workflow, but that will get done later
@app.get('/auth/callback')
def callback_route(code: str):
    API_ENDPOINT = 'https://discord.com/api/v10'
    begging_info = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': CLIENT_URL
    }
    define_begging ={
        'Content-Type': 'application/x-www-form-urlencoded'

    }
    response = requests.post(f'{API_ENDPOINT}/oauth2/token', data=begging_info, headers=define_begging,auth=(CLIENT_ID, CLIENT_SECRET))
    response.raise_for_status()
    meow = response.json()
    token = meow['access_token']
    
    token_header = {
        'Authorization': f'Bearer {token}'
    }
    
    user_data = requests.get('https://discord.com/api/v10/users/@me', headers = token_header)
    user_data.raise_for_status()
    user_id = user_data.json()['id']
    RedirectResponse(url = f'/submissions/{user_id}')
    return('Redirected')
