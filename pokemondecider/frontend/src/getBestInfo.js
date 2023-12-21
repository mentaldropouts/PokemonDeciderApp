import { statData } from "./Stats"
import { typeData } from "./Types"
import { useState } from 'react'

const GetBestInfo = async ( bestPokemonNames ) => {
    const pokemonInfo = useState([])
    let PokemonNumber = 0
    console.log(statData.length)
    for (let i = 0; i < statData.length; i++) {
    console.log("STATDATA at ", statData[toString(i)])
     if (statData[i]["Name"] === bestPokemonNames[PokemonNumber]) {
        PokemonNumber = PokemonNumber + 1

        console.log("found ", bestPokemonNames[PokemonNumber])
     }
   }
 };

 export default GetBestInfo