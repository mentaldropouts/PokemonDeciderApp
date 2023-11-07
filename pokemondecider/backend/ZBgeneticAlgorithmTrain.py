import pygad
import numpy
import json

f = open('FullPokemonStats.json')
pokemonData = json.load(f)
f.close()

f = open('FullPokemonTypes.json')
typeData = json.load(f)
f.close()

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

    pokemonTeamIDGood = [445,130,36,530,593,212]
    pokemonTeamIDBad = [53,505,295,508,203,428]


    team_function_inputs1 = createTeamArrLong(pokemonTeamIDGood, pokemonData, typeData)
    print(pokemonTeamIDGood)
    print()

    team_function_inputs2 = createTeamArrLong(pokemonTeamIDBad, pokemonData, typeData)
    print(pokemonTeamIDBad)
    print()




    inputs = [team_function_inputs1, team_function_inputs2]
    desired_outputGood = 1000 # Function 1 output.
    desired_outputBad = 0 # Function 2 output.
    desired_outputs = [1000,0]

    #Origional function from PyGAD website
    # def fitness_func(ga_instance, solution, solution_idx):
    #     output1 = numpy.sum(solution*function_inputs1)
    #     output2 = numpy.sum(solution*function_inputs2)
    #     fitness1 = 1.0 / (numpy.abs(output1 - desired_output1) + 0.000001)
    #     fitness2 = 1.0 / (numpy.abs(output2 - desired_output2) + 0.000001)
    #     return [fitness1, fitness2]

    def fitness_func(ga_instance, solution, solution_idx):
        outputs = [0] * len(inputs)
        fitnesses = [0] * len(inputs)
        for i in range(len(inputs)):
            outputs[i] = numpy.sum(solution*inputs[i])
            fitnesses[i] = 1.0/(numpy.abs(outputs[i] - desired_outputs[i]) + 0.000001)
        
        return fitnesses

    num_generations = 5000
    num_parents_mating = 30

    sol_per_pop = 50
    num_genes = len(team_function_inputs1)

    ga_instance = pygad.GA(num_generations=num_generations  ,
                        num_parents_mating=num_parents_mating,
                        sol_per_pop=sol_per_pop,
                        num_genes=num_genes,
                        fitness_func=fitness_func,
                        parent_selection_type='nsga2')

    ga_instance.run()

    # ga_instance.plot_fitness(label=['Obj 1', 'Obj 2'])

    solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)


    # Convert the best solution (weights) to a JSON-serializable format
    solution_dict = {
        "best_solution": solution.tolist()  # Convert the numpy array to a Python list
    }

    # Save the best solution to a JSON file
    with open('best_solution.json', 'w') as file:
        json.dump(solution_dict, file)

    print(f"Parameters of the best solution : {solution}")
    print(f"Fitness value of the best solution = {solution_fitness}")

    prediction = numpy.sum(numpy.array(team_function_inputs1)*solution)
    print(f"Predicted output 1 based on the best solution : {prediction}")
    prediction = numpy.sum(numpy.array(team_function_inputs2)*solution)
    print(f"Predicted output 2 based on the best solution : {prediction}")

    test_team_ids = [10, 20, 30, 40, 50, 60]  # Replace with your test team IDs
    test_team_inputs = createTeamArrLong(test_team_ids, pokemonData, typeData)

    # Use the best solution obtained from the genetic algorithm
    best_solution = solution

    result, prediction = evaluate_team(test_team_inputs, best_solution)

    if result == 1:
        print("The test team is good with a score of: " , prediction)
    else:
        print("The test team is bad with a score of: " , prediction)
