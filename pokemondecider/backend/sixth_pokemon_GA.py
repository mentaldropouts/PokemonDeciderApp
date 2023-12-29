import random
import numpy as np
import pandas as pd
import os

test = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon"]

class GenAlg:

    def __init__(self, fileName, maxGenerations=500, populationSize=20, mutationRate=0.1):
        """
        Initializes the Genetic Algorithm with specified parameters.

        Purpose:
            - Set up the genetic algorithm with user-defined parameters.
        
        Input:
            - fileName (str): Path to the Pokemon data file.
            - maxGenerations (int): Maximum number of generations.
            - populationSize (int): Size of the population in each generation.
            - mutationRate (float): Probability of mutation for each individual.
        """
        self.file = fileName
        self.teamSize = 6
        self.maxGen = maxGenerations
        self.popSize = populationSize
        self.mutRate = mutationRate
        self.user_pokemon = test
        self.gen = None

    def find_6th_best_pokemon(self):
        """
        Recommends the 6th best Pokemon based on type effectiveness and stats.

        Purpose:
            - Suggests a Pokemon whose types are effective against potential threats.

        Output:
            - str: Name of the recommended 6th Pokemon.
        """
        best_6th_pokemon = None
        best_6th_stats = np.zeros(6)  # Initialize with zeros
        
        for pokemon_name in self.gen['Name']:
            cleaned_pokemon_name = pokemon_name.strip()
            if cleaned_pokemon_name not in self.user_pokemon:
                total_stats = self.gen.loc[self.gen['Name'] == pokemon_name, 'HP':'Speed'].values.sum()

                type_effectiveness = np.zeros(18)  # 18 = num of types

                for user_choice in self.user_pokemon:
                    cleaned_user_choice = user_choice.strip()
                    if cleaned_user_choice not in self.gen['Name'].values:
                        print(f"User's PokÃ©mon '{user_choice}' not found in the dataset.")
                        continue

                    user_choice_types = self.gen.loc[self.gen['Name'] == cleaned_user_choice, 'Type 1':'Type 2'].values
                    user_choice_types = [t for t in user_choice_types.flatten() if t != 'None']
                    pokemon_types = set(self.gen.loc[self.gen['Name'] == pokemon_name, 'Type 1':'Type 2'].values.flatten())

                    for t in user_choice_types:
                        if t in pokemon_types:
                            type_index = list(pokemon_types).index(t)
                            type_effectiveness += self.damageArray[type_index]

                reverse_type_effectiveness = np.ones(18) - type_effectiveness
                combined_effectiveness = total_stats * reverse_type_effectiveness

                if combined_effectiveness.sum() > best_6th_stats.sum():
                    best_6th_stats = combined_effectiveness
                    best_6th_pokemon = pokemon_name

        return best_6th_pokemon

    def fitness(self, pokemon_team):
        """
        Calculates the fitness or total stats of a given Pokemon team.

        Purpose:
            - Evaluates the fitness of a Pokemon team based on type coverage and total stats.

        Input:
            - pokemon_team (list): List of Pokemon names representing the team.

        Output:
            - int: Fitness score of the team.
        """
        team_stats = self.gen[self.gen['Name'].isin(pokemon_team)].sum()
        total_stats = team_stats['HP'] + team_stats['Attack'] + team_stats['Defense'] + team_stats['SpAtk']  + team_stats['SpDef'] + team_stats['Speed']
        typeCoverage = sum(1 for value in self.teamTypes.values() if value > 0)

        return typeCoverage * total_stats

    def create_random_slots(self, gen):
        """
        Creates a random Pokemon team by filling empty slots.

        Purpose:
            - Generates a random Pokemon team by filling empty slots.

        Input:
            - gen (pd.DataFrame): DataFrame containing Pokemon data.

        Output:
            - list: Randomly generated Pokemon team.
        """
        numRandomSlots =  6 - len(self.user_pokemon)
        randMon = random.sample(gen['Name'].tolist(), numRandomSlots)
        randMon = self.user_pokemon + randMon

        return randMon

    def crossover(self, parent1, parent2):
        """
        Creates offspring from two parent Pokemon teams.

        Purpose:
            - Produces offspring by combining genetic material from two parent teams.

        Input:
            - parent1 (list): First parent Pokemon team.
            - parent2 (list): Second parent Pokemon team.

        Output:
            - list: Offspring Pokemon team.
        """
        midpoint = self.teamSize // 2
        offspring = parent1[:midpoint] + parent2[midpoint:]
        return offspring

    def mutate(self, pokemon_team, mutation_rate, gen):
        """
        Mutates a Pokemon team by randomly replacing one Pokemon with another.

        Purpose:
            - Introduces random changes to a Pokemon team.

        Input:
            - pokemon_team (list): Pokemon team to be mutated.
            - mutation_rate (float): Probability of mutation.
            - gen (pd.DataFrame): DataFrame containing Pokemon data.
        """
        if random.random() < mutation_rate:
            i = 0
            while pokemon_team[i] in self.user_pokemon:
                i = random.randint(0, self.teamSize - 1)
            new_pokemon = random.choice(gen['Name'].tolist())
            pokemon_team[i] = new_pokemon

    def countTypes(self):
        """
        Counts the types of Pokemon in the user's team.

        Purpose:
            - Counts the occurrences of each Pokemon type in the user's team.

        Output:
            - dict: Dictionary with Pokemon types as keys and counts as values.
        """
        teamTypes = {type_: 0 for type_ in self.types}
        for i in self.user_pokemon:
            if (i == ""):
                continue
            currentRow = self.gen.loc[self.gen['Name'] == i]
            teamTypes[currentRow['Type 1'].values[0]] += 1
            if currentRow['Type 2'].values[0] != 'None':
                teamTypes[currentRow['Type 2'].values[0]] += 1
        
        self.teamTypes = teamTypes

    def genDriver(self):
        """
        Initializes the Genetic Algorithm by reading data and setting up variables.

        Purpose:
            - Sets up necessary variables and data for the Genetic Algorithm.
        """
        self.damageArray = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                        [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                        [1, 2, 1/2, 1, 1, 1, 2, 1, 1, 1, 1/2, 1],
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
        
        # Reading and cleaning data
        print("Reading File", self.file)
        try:
            self.gen = pd.read_csv(self.file).drop('ID', axis=1)
        except Exception as e:
            print(f"Error reading this file:{e}")
        
        self.gen = self.gen[~self.gen['Name'].str.contains("Mega", case=False)]    
        self.gen['Type 2'].fillna('None', inplace=True)

        # Removing Legendary and Mega
        filtered_OP = self.gen[self.gen['Total'] > 600]
        self.gen = self.gen.drop(filtered_OP.index)
        assert len(self.gen) > 200

    def run(self):
        """
        Executes the main Genetic Algorithm loop.

        Purpose:
            - Runs the main loop of the Genetic Algorithm to evolve Pokemon teams.
        """
        best_6th_pokemon = None
        self.countTypes()

        print(self.user_pokemon, "\n")
        print("Number of Pokemon: ", len(self.user_pokemon))

        print("Populating")
        print(self.create_random_slots(self.gen))

        population = [self.create_random_slots(self.gen) for _ in range(self.popSize)]

        for generation in range(self.maxGen):
            fitness_scores = [self.fitness(team) for team in population]
            num_parents = self.popSize // 2
            parents = [population[i] for i in sorted(range(len(fitness_scores)), key=lambda x: fitness_scores[x], reverse=True)[:num_parents]]      

            new_generation = []
            while len(new_generation) < self.popSize:
                parent1, parent2 = random.sample(parents, 2)
                offspring = self.crossover(parent1, parent2)
                self.mutate(offspring, self.mutRate, self.gen)
                new_generation.append(offspring)

            population = new_generation

        best_team = max(population, key=self.fitness)
        best_fitness = self.fitness(best_team)
        best_6th_pokemon = self.find_6th_best_pokemon()

        self.bestTeam = best_team
        self.bestPokemon = best_6th_pokemon

# Example usage:
# Model = GenAlg(fileName="pokemondecider/backend/PokemonStats.csv")
# Model.genDriver()
# Model.run()