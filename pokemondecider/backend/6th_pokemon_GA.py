import random
import numpy as np
import pandas as pd


global team_size
team_size = 6

print("Starting")
#Recommends Pokemon whose types are effective against the types that may be a threat to current team.
def find_6th_best_pokemon(user_pokemon, gen1, damage_array):
    print("starting")
    best_6th_pokemon = None
    best_6th_stats = np.zeros(6)  # Initialize with zeros

    #Iterating thorugh each pokemon in gen1
    for pokemon_name in gen1['Name']:
        #Clean the pokemon name by removing leading and trailing spaces
        cleaned_pokemon_name = pokemon_name.strip()
        #If pokemon is not already chosen by the user
        if cleaned_pokemon_name not in user_pokemon:
            # Calculate the total stats for the 6th Pokémon
            total_stats = gen1.loc[gen1['Name'] == pokemon_name, 'HP':'Speed'].values.sum()

            # Calculate type effectiveness based on user's chosen Pokémon
            type_effectiveness = np.zeros(18)  #18 = num of types
            for user_choice in user_pokemon:
                cleaned_user_choice = user_choice.strip()
                #Check if input pokemon is in dataset
                if cleaned_user_choice not in gen1['Name'].values:
                    print(f"User's Pokémon '{user_choice}' not found in the dataset.")
                    continue

                #Types of user's chosen pokemon
                user_choice_types = gen1.loc[gen1['Name'] == cleaned_user_choice, 'Type 1':'Type 2'].values
                #ignoring 'None' (if pokemon has no second type)
                user_choice_types = [t for t in user_choice_types.flatten() if t != 'None']  # Convert to list
                #get types of 6th pokemon
                pokemon_types = set(gen1.loc[gen1['Name'] == pokemon_name, 'Type 1':'Type 2'].values.flatten())

                #Calculating type effectiveness using the damage_array
                for t in user_choice_types:
                    if t in pokemon_types:
                        type_index = list(pokemon_types).index(t)
                        type_effectiveness += damage_array[type_index]

                # Calculate reverse type effectiveness score to find complementing types
                reverse_type_effectiveness = np.ones(18) - type_effectiveness

            # Combine total stats and type effectiveness score
            combined_effectiveness = total_stats * reverse_type_effectiveness

            #if combined score is higher than the current best
            if combined_effectiveness.sum() > best_6th_stats.sum():
                best_6th_stats = combined_effectiveness
                best_6th_pokemon = pokemon_name

    return best_6th_pokemon

#Calculates the fitness or total stats of a given Pokemon team
def fitness(pokemon_team, gen1):
    team_stats = gen1[gen1['Name'].isin(pokemon_team)].sum()
    total_stats = team_stats['HP'] + team_stats['Attack'] + team_stats['Defense'] + team_stats['Sp. Atk']  + team_stats['Sp. Def'] + team_stats['Speed']
    
    return total_stats

#Creates random pokemon team
def create_random_team(gen1):
    team = random.sample(gen1['Name'].tolist(), team_size)
    return team

#Creates offsprint from two parent pokemon teams
def crossover(parent1, parent2):
    #Finds midpoint of teams
    midpoint = team_size // 2
    #Offspring = First half of parent 1 + second half of parent 2
    offspring = parent1[:midpoint] + parent2[midpoint:]
    return offspring

#Mutate by randomly replacing one pokemon with another
def mutate(pokemon_team, mutation_rate, gen1):
    team_size = 6
    if random.random() < mutation_rate:
        #random index
        i = random.randint(0, team_size - 1)
        #Replace Pokemon at index with a randomly chosen pokemon
        new_pokemon = random.choice(gen1['Name'].tolist())
        pokemon_team[i] = new_pokemon


def driver(user_pokemon):

#Reading and cleaning data
    gen1 = pd.read_csv('PokemonStats.csv').drop('#', axis=1)

    mask = gen1['Name'].str.startswith('Mega')

    gen1 = gen1[~mask]

    # gen1 = gen1[gen1['Generation'] == 1].reset_index() #Generation 1

    gen1['Total'] = gen1['HP'] + gen1['Attack'] + gen1['Defense'] + gen1['SpAtk'] + gen1['SpDef'] + gen1['Speed']

    gen1['Type 2'].fillna('None', inplace=True)

    gen1.drop(['index', 'Generation', 'Legendary', 'Total'], axis=1, inplace=True)

#Uncomment below to see data
# print(gen1.info())

    #Constants
    team_size = 6
    max_generations = 750
    population_size = 20
    mutation_rate = .1

    #Storing all 18 possible pokemon types in an array
    pokemon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                    "Fighting", "Poison", "Ground", "Flying", "Psychic",
                    "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

    #18 x 18 array with Pokemon type multipler values
    damage_array = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                    [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
                    [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
                    [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
                    [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
                    [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
                    [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
                    [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
                    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
                    [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
                    [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
                    [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
                    [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
                    [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]])

    # #Asking User for 5 Pokemon
    # user_pokemon = []
    # for i in range(5):
    #     user_pokemon_name = input(f"Enter the name of Pokémon {i+1}: ")
    #     user_pokemon.append(user_pokemon_name)

    #Variables for 6th pokemon and its stats
    best_6th_pokemon = None

    #Generating initial population of random pokemon teams
    population = [create_random_team() for _ in range(population_size)]

    #Loop that runs every generation
    for generation in range(max_generations):
        #Calculate fitness scores for teams
        fitness_scores = [fitness(pokemon_team) for pokemon_team in population]

        #Select half of population as parents
        num_parents = population_size // 2
        parents = [population[i] for i in sorted(range(len(fitness_scores)), key=lambda x: fitness_scores[x], reverse=True)[:num_parents]]
    
        #Generate new generation using crossovers and mutations
        new_generation = []
        while len(new_generation) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            offspring = crossover(parent1, parent2)
            mutate(offspring)
            new_generation.append(offspring)

        #Updating population with newly generated generation
        population = new_generation

    #'Best' variables
    best_team = max(population, key=fitness)
    best_fitness = fitness(best_team)
    best_6th_pokemon = find_6th_best_pokemon(user_pokemon)

    #Output
    print("Best 6th Pokemon for your team:", best_6th_pokemon)

# print("Best Team: ", best_team)
# print("Total Stats of Best Team: ", best_fitness)