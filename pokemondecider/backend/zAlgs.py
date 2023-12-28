import json
import random
import copy
import csv

def createRandTeamOfFive(dataSet):
    team = {}
    dataSize = len(dataSet)
    print(dataSize)
    for i in range(5):
        num = str(random.randint(1, len(dataSize)))
        newPokemon = dataSet[num]
        newPokemon["ID"] = num
        team[i] = newPokemon
    return team

# * works for any size team as long as it is in the format of a dictionary such as {{memberNum : memberStats}, ...}
def getTeamStrengths(team, pokemonTypes, typeStrengths, typeList):
    # * initialize dict where typing is key and values are 0
    teamStrengths = {type: 0 for type in typeList}
    for pokemon in team:
        # * get types for each pokemon
        types = pokemonTypes[team[pokemon]["ID"]]
        for type in types:
            # * get strengths for each type
            tempStrengths = typeStrengths[type]
            for strength in tempStrengths:
                # * check that strength is formatted correctly
                if strength not in teamStrengths:
                    print("Invalid strength String --", strength, "--.")
                    return False
                teamStrengths[strength] += 1    # * adjust values
    return teamStrengths
    
# * works for any size team as long as it is in the format of a dictionary such as {{memberNum : memberStats}, ...}
def getTeamWeaknesses(team, pokemonTypes, typeWeaknesses, typeList):
    # * initialize dict where typing is key and values are 0
    teamWeaknesses = {type: 0 for type in typeList}
    for pokemon in team:
        # * get types for each pokemon
        types = pokemonTypes[team[pokemon]["ID"]]
        for type in types:
            # * get strengths for each type
            tempWeaknesses = typeWeaknesses[type]
            for weakness in tempWeaknesses:
                # * check that strength is formatted correctly
                if weakness not in teamWeaknesses:
                    print("Invalid strength String --", weakness, "--.")
                    return False
                teamWeaknesses[weakness] += 1   # * adjust values
    return teamWeaknesses

# * finds optimal sixth pokemon for your team of five
def findOptimalSixth(initialTeam, pokemonTypes, typeStrengths, typeWeaknesses, typeList, dataSet):
    bestScore = 0
    bestID = ""
    testTeam = initialTeam.copy()  # Create a copy of initialTeam
    finalTeam = initialTeam.copy()  # Create a copy of initialTeam

    for pokemon in dataSet:
        testPokemonStats = copy.deepcopy(dataSet[pokemon])  # Create a deep copy of the dictionary
        testPokemonStats["ID"] = pokemon
        testTeam[5] = testPokemonStats

        testScore = calculateScore(testTeam, pokemonTypes, typeStrengths, typeWeaknesses, typeList)
        if testScore > bestScore:
            bestScore = testScore
            bestID = pokemon
            finalTeam[5] = testPokemonStats
        
        print("test pokemon score: %.3f" % testScore,"--", dataSet[pokemon]["Name"], "| best score so far: %.3f" % bestScore, "--", dataSet[bestID]["Name"])
   
    return finalTeam

# * calculate the score for a team of six given the coverage(either initialStrengths or initialWeaknesses) and return an int
# * scales to give more weight to the coverage types of lesser value to increase width of coverage
def calculateScore(members, pokemonTypes, typeStrengths, typeWeaknesses, typeList):
    score = 0

    testStrengths = getTeamStrengths(members, pokemonTypes, typeStrengths, typeList)
    testWeaknesses = getTeamWeaknesses(members, pokemonTypes, typeWeaknesses, typeList)

    for member in members:
        for strength in testStrengths:
            score += ((1 / testStrengths[strength]) if testStrengths[strength] != 0 else 1)
        
        for weakness in testWeaknesses:
            score += ((1 / testWeaknesses[weakness]) if testWeaknesses[weakness] != 0 else 1)

    return score

# * takes a list of ID numbes and creates a team in the form of a dictionary that includes all the stats
# * just like it is for other functions and is standard thus far
# * works for any number of pokemon

def createTeam(pokedexNumArr, dataSet):
    print("CREATING TEAM")
    newTeam = {}
    for i in range(len(pokedexNumArr)):
        # * check if team already contains pokemon as a team cannot have duplicate pokemon.
        print()
        if int(pokedexNumArr[i]) not in newTeam:
            newTeam[pokedexNumArr[i]] = dataSet[pokedexNumArr[i]]
            print("new added ", newTeam[pokedexNumArr[i]] )
            newTeam[pokedexNumArr[i]]["ID"] = pokedexNumArr[i]
        else:
            print("Pokemon \"", pokedexNumArr[i], ":", dataSet[str(pokedexNumArr[i])]["Name"], "\" is a duplicate and cannot be added")

    return newTeam



def load_csv(file_path, key_column):
    try:
        with open(file_path, newline='') as csvfile:
            csv_data = csv.DictReader(csvfile)
            return {int(row[key_column]): row for row in csv_data}
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except Exception as e:
        print(f"Error loading CSV from '{file_path}': {e}")
        return None


def createTeamDriver():

    print("Running createTeamDriver!")
    # Purpose: to handle the json files and utilitze those to create teams 
    # in a function that can be called externally by a flask route

    # Load CSV data
    FULLPOKEMONSTATS = load_csv('stats.csv','ID')

    print(FULLPOKEMONSTATS[1])
    if any(data is None for data in [FULLPOKEMONSTATS]):
        return 0


    TYPELIST = [
    "Normal", "Fire", "Water", "Grass", "Electric",
    "Ice", "Fighting", "Poison", "Ground", "Flying",
    "Psychic", "Bug", "Rock", "Ghost", "Dark", "Steel",
    "Fairy", "Dragon"]

    # For testing functionallity
    pokemonList = [1,2,3,5,6]
    # For Generating random team
    randomList = random.sample(range(0,len(FULLPOKEMONSTATS)),5)
    print(randomList)
    newTeam = createTeam(randomList,FULLPOKEMONSTATS)

    # for pokemon in newTeam:
        # print(pokemon,": ", newTeam[pokemon], end="\n")
        # print()

    print("NEW TEAM FULL", newTeam) 
    return newTeam

# if __name__ == '__main__':
    # * initailize data for calculations
    # * {ID: [Name,Total,HP,Attack,Defense,SpAtk,SpDef,Speed,Height,Weight],...}
    

    # createTeamDriver()


    # # * {numInTeam: [PokedexNum,Name,Total,HP,Attack,Defense,SpAtk,SpDef,Speed,Height,Weight],...}
    # teamOfFive = createRandTeamOfFive(FULLPOKEMONSTATS)
    # for pokemon in teamOfFive:
    #     print(pokemon,": ", teamOfFive[pokemon])

    # teamOfSix = findOptimalSixth(teamOfFive, POKEMONTYPES, TYPESTRENGTHS, TYPEWEAKNESSES, TYPELIST, FULLPOKEMONSTATS)
    # print("New best team of Six")
    # for pokemon in teamOfSix:
    #     print(pokemon,": ", teamOfSix[pokemon])
