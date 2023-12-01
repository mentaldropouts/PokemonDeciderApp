from flask import Flask, request, jsonify
from zAlgs import createTeamDriver
from flask_cors import CORS
from sixth_pokemon_GA import GenAlg

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


@api.route('/buttonPressed', methods=['POST'])
def button_pressed():
    try:
        # Assuming the request contains JSON data with a key 'buttonPressed'
        print("Getting Button")
        button_pressed = request.json.get('buttonPressed')

        # Perform some action based on the button_pressed value
        if button_pressed:
            # Perform an action when the button is pressed
            result = {'message': 'Button pressed on the frontend!'}
            print(result)
            # print(pokemonTeam)
            Model = GenAlg("PokemonStats.csv")
            Model.user_pokemon = list(pokemonTeam.values())
            Model.genDriver()
            Model.run()

            print("Best Pokemon: ", Model.bestPokemon)
            


        else:
            result = {'message': 'Button not pressed.'}
            print(result)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@api.route('/PokeData', methods=['POST', 'OPTIONS'])
def receive_data_from_frontend():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'message': 'Preflight request successful'})
    else:
        try:
            data_from_frontend = request.get_json()
            
            print(data_from_frontend["name"], ":", data_from_frontend["label"]["label"])   
        
            currentName = data_from_frontend["name"]

            currentLabel = data_from_frontend["label"]["label"]

            pokemonTeam[currentLabel] = currentName
            # Process the data as needed

            print(pokemonTeam)
            print()

            response = jsonify({'message': 'Data received and processed successfully'})
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            response = jsonify({'error': 'Internal Server Error'}), 500

    # Set CORS headers for the main request
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')


    return response