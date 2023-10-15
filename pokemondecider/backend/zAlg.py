import json
import random
import copy
def createRandTeamOfFive(dataSet):
    team = {}
    dataSize = len(dataSet)
    for i in range(5):
        num = str(random.randint(1, 150))

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
    newTeam = {}
    for i in range(len(pokedexNumArr)):
        # * check if team already contains pokemon as a team cannot have duplicate pokemon.
        if pokedexNumArr[i] not in newTeam:
            newTeam[pokedexNumArr[i]] = dataSet[str(pokedexNumArr[i])]
            newTeam[pokedexNumArr[i]]["ID"] = pokedexNumArr[i]
        else:
            print("Pokemon \"", pokedexNumArr[i], ":", dataSet[str(pokedexNumArr[i])]["Name"], "\" is a duplicate and cannot be added")
    return newTeam

if __name__ == '__main__':
    # * initailize data for calculations
    # * {ID: [Name,Total,HP,Attack,Defense,SpAtk,SpDef,Speed,Height,Weight],...}
    f = open('pokemondecider/backend/Data/FULLPokemonStats.json')
    FULLPOKEMONSTATS = json.load(f)
    f.close()
    f = open('pokemondecider/backend/Data/FullPokemonTypes.json')
    POKEMONTYPES = json.load(f)
    f.close()
    f = open('pokemondecider/backend/Data/TypeStrengths.json')
    TYPESTRENGTHS = json.load(f)
    f.close()
    f = open('pokemondecider/backend/Data/TypeWeaknesses.json')
    TYPEWEAKNESSES = json.load(f)
    f.close()
    f = open('pokemondecider/backend/Data/TypeImmunities.json')
    TYPEIMMUNITIES = json.load(f)
    f.close()

    TYPELIST = [
    "Normal", "Fire", "Water", "Grass", "Electric",
    "Ice", "Fighting", "Poison", "Ground", "Flying",
    "Psychic", "Bug", "Rock", "Ghost", "Dark", "Steel",
    "Fairy", "Dragon"]

    pokemonList = [1,2,3,5,6]
    newTeam = createTeam(pokemonList,FULLPOKEMONSTATS)
    for pokemon in newTeam:
        print(pokemon,": ", newTeam[pokemon], end="\n")


    # # * {numInTeam: [PokedexNum,Name,Total,HP,Attack,Defense,SpAtk,SpDef,Speed,Height,Weight],...}
    # teamOfFive = createRandTeamOfFive(FULLPOKEMONSTATS)
    # for pokemon in teamOfFive:
    #     print(pokemon,": ", teamOfFive[pokemon])

    # teamOfSix = findOptimalSixth(teamOfFive, POKEMONTYPES, TYPESTRENGTHS, TYPEWEAKNESSES, TYPELIST, FULLPOKEMONSTATS)
    # print("New best team of Six")
    # for pokemon in teamOfSix:
    #     print(pokemon,": ", teamOfSix[pokemon])

 