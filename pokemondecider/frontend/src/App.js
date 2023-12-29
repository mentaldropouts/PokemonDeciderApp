import './App.css';
import  PokemonDropdown  from "./front"
// import GetBestInfo from './getBestInfo'
import handleButtonClick from './sendButton'
import { statData } from './Stats';
import getRandomData from './sendRandTeam';
import { useState, useEffect } from'react'
import BestPokemon from './frontBest';



function App() {
  const [bestPokemonName, setBestPokemonName] = useState("");
  const [RandTeam, setRandTeam] = useState();
  const bestPokemonID = []

  useEffect(() => {
    // This code will run after bestPokemonData has been updated
    const div = document.getElementById("10");
    const button = document.getElementById('9');
    button.style.backgroundColor = '#e75c37';
    div.textContent = bestPokemonName;

}, [bestPokemonName]);  


function findKeyByValue(obj, value) {
  return new Promise((resolve, reject) => {
    Object.keys(obj).forEach(key => {
      if (obj[key]["Name"] === value) {
        resolve(key);
      }
    });
    reject(new Error("Key not found"));
  });
}

// Define a function to receive random team data
  async function handleTeamDataRandom() {
    try {
      const result = await  getRandomData();
      setRandTeam(result)
      } catch (error) {
        console.error('Error fetching data in App.js:', error);
      }
  }

  async function handleTeamDataLoaded() {
    try {
      const button = document.getElementById('9');
      button.style.backgroundColor = 'green';
      const result = await handleButtonClick();
      button.style.backgroundColor = '#e75c37';

      //#######################################################################
      // There is a problem here because the file "Stats.js" does not have 
      // all of the pokemon that FullPokemonStats.json has. Like Shaymin Land
      // Forme is in pokemon.csv but not in the other two files
      //#######################################################################

      // Getting the ID of the resulting best pokemon
      for (const element of result){
        console.log("ELEMENT: ", element)
        console.log("RESULT: ", result)
        const value = await findKeyByValue(statData, element)
        console.log("VALUE: ", value)
        bestPokemonID.append(value)
      }
      
    } catch (error) {
      console.error('Error in handleTeamDataLoaded:', error);
    }
    // console.log("Best ID:", bestPokemonID)
  }

  return (
    <div className="App">
      <h1 class="header">Pokemon Decider</h1>
    
          <div class="dropdownBack">
            <PokemonDropdown label="1" randTeamData={RandTeam}/> 
            <PokemonDropdown label="2" randTeamData={RandTeam}/> 
            <PokemonDropdown label="3" randTeamData={RandTeam}/> 
            <PokemonDropdown label="4" randTeamData={RandTeam}/> 
            <PokemonDropdown label="5" randTeamData={RandTeam}/>
          </div>

          <div class="bestPokemon">
            <div class="buttonRow">
            <button class="Button" id ="8" onClick={handleTeamDataRandom}>Random</button>
            <button class="Button" id ="9" onClick={handleTeamDataLoaded}>Submit</button>
            
            {/* <BestPokemon label="6" ID=/> */}
            <div class="name" id="10"></div>
            </div>
        </div>
    </div>
  );
}

export default App;
