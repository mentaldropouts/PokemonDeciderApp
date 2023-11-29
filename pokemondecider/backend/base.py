from flask import Flask, request, jsonify
from zAlgs import createTeamDriver
from flask_cors import CORS

# This is the basic set up for what we will be using to handle the pokemon data.
# We will handle the data by calling Zach's Algorithms and then send the dict of 
# data that results into a response body that will then be handled by the react 
# front end. I made a file in the frontend called "handler.js" that shows how this
# process is done.

print("Starting Backend")

api = Flask(__name__)
CORS(api)

@api.route('/test')
def randomTeam():
    response_body = createTeamDriver()
    return response_body


pokemonTeam = {}

@api.route('/submit', methods=['POST', 'OPTIONS'])
def receive_data_from_frontend():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'message': 'Preflight request successful'})
    else:
        try:
            data_from_frontend = request.get_json()
            for i in data_from_frontend.keys():
                print(i, ":", data_from_frontend[i])





            # Process the data as needed
            response = jsonify({'message': 'Data received and processed successfully'})
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            response = jsonify({'error': 'Internal Server Error'}), 500

    # Set CORS headers for the main request
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')

    return response