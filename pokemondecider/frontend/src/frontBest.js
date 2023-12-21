import { useState, useEffect } from 'react'
import { statData } from "./Stats"
import { typeData } from "./Types"



function BestPokemon( { label, ID } ) {

    useEffect(() => {
        handleSlottingData()
    }, [ID, label]);


const [selectedPokemonData, setSelectedPokemonData] = useState({
    name: "MissingNo.",
    id: "0",
    total: "0",
    hp: "0",
    attack: "0",
    defense: "0",
    spAtk: "0",
    spDef: "0",
    speed: "0",
    type1: "",
    type2: "",
    image: 'pkmnSprites/pkmn0.png',
    label: {label}
  });

  const handleSlottingData = () => {
    setSelectedPokemonData({
      name: statData[ID].Name,
      id: ID,
      total: statData[ID].Total,
      hp: statData[ID].HP,
      attack: statData[ID].Attack,
      defense: statData[ID].Defense,
      spAtk: statData[ID].SpAtk,
      spDef: statData[ID].SpDef,
      speed: statData[ID].Speed,
      type1: typeData[ID][0],
      type2: typeData[ID][1],
      image: `pkmnSprites/pkmn${ID}.png`,
      label: {label}
    })
  };

  return (
        <div>
        <div class="imageContainer">
            <img class="image" src={selectedPokemonData.image} alt={selectedPokemonData.name} />
            <div class="name"> {selectedPokemonData.name}</div>
        </div>
        
          <div>
            <div class="statsholder">
              <div class="col">
              <div class="statsGrouper"> Attack <div class="stats">{selectedPokemonData.attack}</div></div>
                <div class="statsGrouper"> Defense <div class="stats">{selectedPokemonData.defense}</div></div>
               <div class="statsGrouper"> Total <div class="stats">{selectedPokemonData.total}</div></div>
              </div>
              <div class="col">
                <div class="statsGrouper"> SpAtk <div class="stats">{selectedPokemonData.spAtk}</div> </div>
                <div class="statsGrouper"> SpDef <div class="stats">{selectedPokemonData.spDef}</div></div>
                <div class="statsGrouper"> Speed <div class="stats">{selectedPokemonData.speed}</div></div>
             </div>
            </div>
            <div class="typeholder">
              <div> {selectedPokemonData.type1} {selectedPokemonData.type2}</div>
            </div>  
          </div>
          </div>
        )};

        export default BestPokemon;