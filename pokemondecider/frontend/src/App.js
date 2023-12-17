import './App.css';
import  PokemonDropdown  from "./front"
import handleButtonClick from './sendButton'
import { useState, useEffect } from'react'


function App() {

  // const [RandTeam,SetRandTeam] = useState();
  const [bestPokemonData, setBestPokemonData] = useState("");
  const [RandTeam, setRandTeam] = useState([])

  useEffect(() => {
    // This code will run after bestPokemonData has been updated
    console.log("Best: ", bestPokemonData);
    const div = document.getElementById("10");
    const button = document.getElementById('9');
    button.style.backgroundColor = '#e75c37';
    div.textContent = bestPokemonData;
}, [bestPokemonData]);

// Define a function to receive random team data
  const handleTeamDataRandom = (data) => {
  setRandTeam(data);
  console.log(RandTeam);
  };

  async function handleTeamDataLoaded() {
    try {
      const button = document.getElementById('9');
      button.style.backgroundColor = 'green';
      const result = await handleButtonClick();
      setBestPokemonData(result);
    } catch (error) {
      console.error('Error in handleTeamDataLoaded:', error);
    }
  }

  return (
    <div className="App">
      <h1 class="header">Pokemon Decider</h1>
    
          <div class="dropdownBack">
            <PokemonDropdown label="1"/> <PokemonDropdown label="2"/> <PokemonDropdown label="3"/> <PokemonDropdown label="4"/> <PokemonDropdown label="5"/>
          </div>

          <div class="bestPokemon">
            <div class="buttonRow">
            <button class="Button" id ="9" onClick={handleTeamDataRandom}>Random</button>

            <button class="Button" id ="9" onClick={handleTeamDataLoaded}>Submit</button>
            <div class="name1" id="10"> </div>
            </div>
        </div>
    </div>
  );
}

export default App;
