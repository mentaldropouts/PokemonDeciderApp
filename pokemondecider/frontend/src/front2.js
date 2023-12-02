import { useState, useEffect } from 'react'
import { statData } from "./Stats"
import { typeData } from "./Types"

function BestPokemon({label, Data} ) {

  console.log("Inside Best: ", Data)

  const findPokemonByName = (name) => {
    return new Promise((resolve, reject) => {
      try {
        const entry = Object.entries(statData).find(([key, pokemon]) => pokemon.Name === name);
        console.log("Entry: ", entry);
        
        if (entry) {
          resolve({ key: entry[0], data: entry[1] });
        } else {
          resolve(null);
        }
      } catch (error) {
        reject(error);
      }
    });
  };



const myDiv = document.getElementById('Name');

// Use the promise and update the div when it's resolved
Data.then((resolvedValue) => {
  const value = Data // Assuming resolvedValue has the structure you described
  console.log(value);

  // Set text content of the div when the promise is fulfilled
  myDiv.textContent = value;
}).catch((error) => {
  console.error(error); // Handle errors here if the promise is rejected
}); 

  // const pokemonData = findPokemonByName(Data)
  
  // console.log("Pokemon Data: ", {pokemonData})

  const [teamData, setTeamData] = useState({

    total: "0",

    hp: "0",

    attack: "0",

    defense: "0",

    spAtk: "0",

    spDef: "0",

    speed: "0",

  })

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

  });

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

    image: `pkmnSprites/pkmn${ID}.png`


    })
  };


      // Shartending the name of the pokemon to be displayed
      const onDataChange = (event) => {
        handleSlottingData(event);
      };

    // Defines the teammate number above the dropdown column
    let pkmnCounter = 0;

    useEffect(() => {

      if (selectedPokemonData.id) {

        console.log(selectedPokemonData.image);

      }

    }, [selectedPokemonData.id])

    return (


          
          <div class="sixthholder">

          <div class="imageContainer">
              <img class="image" src={selectedPokemonData.image} alt={selectedPokemonData.name} />
              <div class="name"> {selectedPokemonData.name}</div>
            
          </div>

          {selectedPokemonData && (

<div>

  {/* <div>Selected Pokemon: {selectedPokemon} </div> */}

  {/* <div>ID: {selectedID}</div> */}

  <div class="bestholder">

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
      // {/* </div> */}
    // </div>

    );

  }
  
  export default BestPokemon;