from flask import Flask


# This is the basic set up for what we will be using to handle the pokemon data.
# We will handle the data by calling Zach's Algorithms and then send the dict of 
# data that results into a response body that will then be handled by the react 
# front end. I made a file in the frontend called "handler.js" that shows how this
# process is done.


api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body