import random
import numpy as np
import pandas as pd


test = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon"]

class GenAlg:

    def __init__(self,fileName, maxGenerations = 750, populationSize = 20, mutationRate = 0.1):

        self.file = fileName
        self.teamSize = 6
        self.maxGen = maxGenerations
        self.popSize = populationSize
        self.mutRate = mutationRate
        self.user_pokemon = test

        
        


    #Recommends Pokemon whose types are effective against the types that may be a threat to current team.
    def find_6th_best_pokemon(self, user_pokemon):
        print("Starting 6th Best Function")

        best_6th_pokemon = None
        best_6th_stats = np.zeros(6)  # Initialize with zeros

        #Iterating thorugh each pokemon in gen
        for pokemon_name in self.gen['Name']:
            #Clean the pokemon name by removing leading and trailing spaces
            cleaned_pokemon_name = pokemon_name.strip()
            #If pokemon is not already chosen by the user
            if cleaned_pokemon_name not in self.user_pokemon:
                # Calculate the total stats for the 6th Pokémon
                total_stats = self.gen.loc[self.gen['Name'] == pokemon_name, 'HP':'Speed'].values.sum()

                # Calculate type effectiveness based on user's chosen Pokémon
                type_effectiveness = np.zeros(18)  #18 = num of types
                for user_choice in user_pokemon:
                    cleaned_user_choice = user_choice.strip()
                    #Check if input pokemon is in dataset
                    if cleaned_user_choice not in self.gen['Name'].values:
                        print(f"User's Pokémon '{user_choice}' not found in the dataset.")
                        continue

                    #Types of user's chosen pokemon
                    user_choice_types = self.gen.loc[self.gen['Name'] == cleaned_user_choice, 'Type 1':'Type 2'].values
                    #ignoring 'None' (if pokemon has no second type)
                    user_choice_types = [t for t in user_choice_types.flatten() if t != 'None']  # Convert to list
                    #get types of 6th pokemon
                    pokemon_types = set(self.gen.loc[self.gen['Name'] == pokemon_name, 'Type 1':'Type 2'].values.flatten())

                    #Calculating type effectiveness using the damage_array
                    for t in user_choice_types:
                        if t in pokemon_types:
                            type_index = list(pokemon_types).index(t)
                            type_effectiveness += self.damageArray[type_index]

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
    def fitness(self,pokemon_team):

        team_stats = self.gen[self.gen['Name'].isin(pokemon_team)].sum()
        total_stats = team_stats['HP'] + team_stats['Attack'] + team_stats['Defense'] + team_stats['SpAtk']  + team_stats['SpDef'] + team_stats['Speed']
        typeCoverage = sum(1 for value in self.teamTypes.values() if value > 0)

        return typeCoverage


    #Creates random pokemon team
    def create_random_team(self, gen):
        team = random.sample(gen['Name'].tolist(), self.teamSize)
        return team

    #Creates offsprint from two parent pokemon teams
    def crossover(self,parent1, parent2):
        #Finds midpoint of teams
        midpoint = self.teamSize // 2
        #Offspring = First half of parent 1 + second half of parent 2
        offspring = parent1[:midpoint] + parent2[midpoint:]
        return offspring

    #Mutate by randomly replacing one pokemon with another
    def mutate(self,pokemon_team, mutation_rate, gen):
        
        if random.random() < mutation_rate:
            #random index
            i = random.randint(0, self.teamSize - 1)
            #Replace Pokemon at index with a randomly chosen pokemon
            new_pokemon = random.choice(gen['Name'].tolist())
            pokemon_team[i] = new_pokemon

    def countTypes(self):
        teamTypes = {type_: 0 for type_ in self.types}
        for i in self.user_pokemon:
            currentRow = self.gen.loc[self.gen['Name'] == i]
            teamTypes[currentRow['Type 1'].values[0]] += 1

            if currentRow['Type 2'].values[0] != 'None':
                teamTypes[currentRow['Type 2'].values[0]] += 1

        self.teamTypes = teamTypes

    def genDriver(self):

        self.damageArray = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
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
        
        self.types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                        "Fighting", "Poison", "Ground", "Flying", "Psychic",
                        "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
        

         #Reading and cleaning data
        self.gen = pd.read_csv(self.file).drop('ID', axis=1)

        mask = self.gen['Name'].str.startswith('Mega')

        self.gen = self.gen[~mask]

        # gen = gen[gen['Generation'] == 1].reset_index() #Generation 1

        # self.gen['Total'] = self.gen['HP'] + self.gen['Attack'] + self.gen['Defense'] + self.gen['SpAtk'] + self.gen['SpDef'] + self.gen['Speed']

        self.gen['Type 2'].fillna('None', inplace=True)

        # Removing Lengendary and Mega
        filtered_OP = self.gen[self.gen['Total'] > 600]
        self.gen = self.gen.drop(filtered_OP.index)
        assert len(self.gen) > 200


        # self.gen.drop(['Total'], axis=1, inplace=True)

        #Constants
        # team_size = 6
        # max_generations = 750
        # population_size = 20
        # mutation_rate = .1
        # #Asking User for 5 Pokemon
        # user_pokemon = []
        #         # for i in range(5):
        #     user_pokemon_name = input(f"Enter the name of Pokémon {i+1}: ")
        #     user_pokemon.append(user_pokemon_name)

    def run(self):
        
        print("Starting run function")
        #Variables for 6th pokemon and its stats
        best_6th_pokemon = None
        
        self.countTypes()

        #Generating initial population of random pokemon teams
        population = self.user_pokemon

        #Loop that runs every generation
        for generation in range(self.maxGen):
        #Calculate fitness scores for teams
            fitness_scores = [self.fitness(self.user_pokemon) for self.user_pokemon in population]

            #Select half of population as parents
            num_parents = self.popSize // 2
            parents = [population[i] for i in sorted(range(len(fitness_scores)), key=lambda x: fitness_scores[x], reverse=True)[:num_parents]]
        
            #Generate new generation using crossovers and mutations
            new_generation = []
            while len(new_generation) < self.popSize:
                parent1, parent2 = random.sample(parents, 2)
                offspring = self.crossover(parent1, parent2)
                self.mutate(offspring, self.mutRate, self.gen)
                new_generation.append(offspring)

            #Updating population with newly generated generation
            population = new_generation

        #'Best' variables
        best_team = max(population, key=self.fitness)
        best_fitness = self.fitness(best_team)
        best_6th_pokemon = self.find_6th_best_pokemon(self.user_pokemon)

        #Output
        print("Best 6th Pokemon for your team:", best_6th_pokemon)
        print("Best Team: ", best_team)



        def Driver(self):
            self.genDriver()
            self.run()