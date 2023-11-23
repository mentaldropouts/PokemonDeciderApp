import json
import numpy 

def evaluate_team(test_team, best_solution):
    prediction = numpy.sum(numpy.array(test_team) * best_solution)
    if prediction >= 0.5:  # You can adjust this threshold as needed.
        return 1, prediction  # Good team
    else:
        return 0, prediction  # Bad team


def createTeamArrLong(teamIDs, pokemonData, typeData):
    teamArr = []
    for id in teamIDs:

        teamArr.append(int(pokemonData[str(id)]["stats"]["hp"]))
        teamArr.append(int(pokemonData[str(id)]["stats"]["attack"]))
        teamArr.append(int(pokemonData[str(id)]["stats"]["defense"]))
        teamArr.append(int(pokemonData[str(id)]["stats"]["spattack"]))
        teamArr.append(int(pokemonData[str(id)]["stats"]["spdefense"]))
        teamArr.append(int(pokemonData[str(id)]["stats"]["speed"]))
        teamArr.append(int(pokemonData[str(id)]["weight"]))
        teamArr.append(int(pokemonData[str(id)]["height"]))

        teamArr.append(33)


    return teamArr


if __name__ == "__main__":
    f = open('pokemondecider/backend/Data/FullPokemonStats.json')
    pokemonData = json.load(f)
    f.close()

    f = open('pokemondecider/backend/Data/FullPokemonTypes.json')
    typeData = json.load(f)
    f.close()

    # pokemonTestTeamIDGood = [445,130,36,530,593,212]
    pokemonTestTeamIDGood = [11,13,46,265,10,213]



    team_function_inputs1 = createTeamArrLong(pokemonTestTeamIDGood, pokemonData, typeData)
    print(pokemonTestTeamIDGood)
    print()

    # Load the best solution from the JSON file
    with open('best_solution.json', 'r') as file:
        solution_dict = json.load(file)

    loaded_solution = numpy.array(solution_dict["best_solution"])

    # Now, loaded_solution contains the best solution (weights) that you saved earlier.

    prediction = numpy.sum(numpy.array(team_function_inputs1)*loaded_solution)
    print(f"Predicted output 1 based on the best solution : {prediction}")
