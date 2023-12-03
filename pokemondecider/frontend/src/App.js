import './App.css';
import  PokemonDropdown  from "./front"
import { statData } from './Stats';
import Handler from "./handler"
import { useState, useEffect } from'react';
import BestPokemon from './front2';
import handleButtonClick from './sendButton';


function App() {

  const [RandTeam,SetRandTeam] = useState();
  const [bestPokemonData, setBestPokemonData] = useState("");

  // Define a function to receive the data from Handler
  const handleTeamDataRandom = (data) => {
  SetRandTeam(data);
  console.log(RandTeam);
  };

  async function handleTeamDataLoaded()  {

    const result = await handleButtonClick();

    setBestPokemonData(result)
    console.log("Best: ", bestPokemonData)
    const div = document.getElementById("10")
    div.textContent = bestPokemonData
    
  }

  
  return (

    <div className="App">
      <h1 class="header">Pokemon Decider</h1>
      
          <div class="dropdownBack">
            <PokemonDropdown label="1"/> <PokemonDropdown label="2"/> <PokemonDropdown label="3"/> <PokemonDropdown label="4"/> <PokemonDropdown label="5"/>
          </div>

          <div class="bestPokemon">
            <div class="buttonRow">
            <button class="Button" onClick={handleTeamDataLoaded}> Submit</button>
            <div class="name" id="10"> </div>
            </div>
        </div>
    </div>
  );
}

export default App;
