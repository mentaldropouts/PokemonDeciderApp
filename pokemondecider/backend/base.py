from flask import Flask
from zAlgs import createTeamDriver

# This is the basic set up for what we will be using to handle the pokemon data.
# We will handle the data by calling Zach's Algorithms and then send the dict of 
# data that results into a response body that will then be handled by the react 
# front end. I made a file in the frontend called "handler.js" that shows how this
# process is done.
print("Starting Backend")

api = Flask(__name__)

@api.route('/test')
def randomTeam():
    response_body = createTeamDriver() 
    
    return response_body
