from flask import Flask, request, jsonify
from zAlgs import createTeamDriver
from flask_cors import CORS
from sixth_pokemon_GA import GenAlg

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# This is the base backend function that takes pokemon teams from 
# the frontend. It also sends the best pokemon to the frontend
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("Starting Backend")

api = Flask(__name__)
CORS(api, origins="http://localhost:3001")

@api.route('/RandPokeData')
def randomTeam():
    try:
        response_body = createTeamDriver()
        for i in response_body:
            print("Respnse ", response_body[i]['Name'])
        return response_body
    except Exception as e:
            print(f"An error occurred: {str(e)}")
            response = jsonify({'error': 'Problem Generating Random Team'})

#################################################
# ISSUES: When the submit button is pressed after
# changing one pokemon. The other pokemon are 
# cleared from the dictionary. Only the newly 
# selected one is left. 
#################################################
            
pokemonTeam = {}

@api.route('/buttonPressed', methods=['POST'])
def button_pressed():
    print("CURRENT TEAM: \n", pokemonTeam)
    try:
        # Assuming the request contains JSON data with a key 'buttonPressed'
        print("Getting Button")
        assert len(pokemonTeam) <= 5
        button_pressed = request.json.get('buttonPressed')
        # Perform some action based on the button_pressed value
        if button_pressed:
            # Perform an action when the button is pressed
            result = {'message': 'Button pressed on the frontend!'}
            Model = GenAlg("PokemonStats.csv")
            Model.user_pokemon = list(pokemonTeam.values())
            Model.genDriver()
            Model.run()
            newMons = [x for x in Model.bestTeam if x not in Model.user_pokemon]
            print("Sending ", newMons, "to frontend")
            return jsonify(result=newMons)
        else:
            result = {'message': 'Button not pressed.'}
            print(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/PokeData', methods=['POST', 'OPTxIONS'])
def receive_data_from_frontend():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'message': 'Preflight request successful'})
        return ('', 204)
    else:
        try:
            print("pokemon: ", pokemonTeam, end="\n\n")
            data_from_frontend = request.get_json()
            # print(data_from_frontend["name"], ":", data_from_frontend["label"]["label"])      
            currentName = data_from_frontend["name"]
            currentLabel = data_from_frontend["label"]["label"]
            if (currentName != "MissingNo."):
                pokemonTeam[currentLabel] = currentName
            else:
                print("POPPING: ", currentLabel,end="\n")   
                pokemonTeam.pop(currentLabel)
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