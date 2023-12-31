import { useState, useEffect } from 'react'
import { statData } from "./Stats"
import { typeData } from "./Types"
import sendDataToBackend from './sendTeam'

function PokemonDropdown( { label, Data } ) {
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
    image: 'pkmnSprites/pkmn4.png',
    label: {label}
  });

  const indexValue = parseInt(label, 10) - 1
  useEffect(() => {   
    // Handle changes in Data
    if (Data && Data.length > indexValue) {
      console.log("INDEX: ", indexValue);
      let curPokemon = Data[indexValue];
      // console.log(curPokemon);
      handleRandomData(curPokemon);
    }
  }, [Data, indexValue]);

  const handleRandomData = (curPokemon) =>{
    const ID = curPokemon.ID;
    setSelectedPokemonData({
      name: curPokemon.Name,
      id: curPokemon.ID,
      total: curPokemon.Total,
      hp: curPokemon.HP,
      attack: curPokemon.Attack,
      defense: curPokemon.Defense,
      spAtk: curPokemon.SpAtk,
      spDef: curPokemon.SpDef,
      speed: curPokemon.Speed,
      type1: typeData[ID][0],
      type2: typeData[ID][1],
      image: `pkmnSprites/pkmn${ID}.png`,
      label: {label}
    })
  }

  // handles dropdown operations
  const handleSlottingData = (event) => {
    const ID = event.target.value;

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

      // Shartending the name of the pokemon to be displayed
      const onDataChange = (event) => {
        const name = event.target.value;
        console.log("NAME", name
          );
        handleSlottingData(event);
      };

    useEffect(() => {
      if (selectedPokemonData.id) { 
        sendDataToBackend(selectedPokemonData, label);
      }
    },[selectedPokemonData.id])

    return (

        <div class="dropdown">
        <div>Pokemon {label}</div>
        <label htmlFor="pokemonSelect"></label>
        {/* Select menu for selecting any of the imported pokemon */}
        <select id="pokemonSelect" onChange={onDataChange} value={selectedPokemonData.id}>
  <option value="" disabled>Select a Pokémon</option>
  {Object.keys(statData).map((id) => (
    <option key={id} value={id}>
     {id}:{statData[id].Name}
    </option>
  ))}
</select>
        <div class="imageContainer">
            <img class="image" src={selectedPokemonData.image} alt={selectedPokemonData.name} />
            <div class="name"> {selectedPokemonData.name}</div>
        </div>
        {/* Stats for pokem */}
        {selectedPokemonData && (
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
        )}
      </div>
    );
  }
  
  export default PokemonDropdown;