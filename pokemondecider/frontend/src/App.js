import './App.css';
import PokemonDropdown from "./front";
// import GetBestInfo from './getBestInfo'
import handleButtonClick from './sendButton';
import { statData } from './Stats';
import getRandomData from './sendRandTeam';
import { useState, useEffect } from 'react';
import BestPokemon from './frontBest';

/**
 * Function to find the key of an object by its corresponding value.
 * @param {object} obj - The object to search through.
 * @param {any} value - The value to find the key for.
 * @returns {Promise<string>} - A promise that resolves to the key or rejects with an error.
 */
function findKeyByValue(obj, value) {
  return new Promise((resolve, reject) => {
    Object.keys(obj).forEach(key => {
      if (obj[key] === value) {
        resolve(key);
      }
    });
    reject(new Error("Key not found"));
  });
}

/**
 * Main component for the Pokemon Decider app.
 * @returns {JSX.Element} - The React component representing the app.
 */
function App() {
  const [bestPokemonName, setBestPokemonName] = useState("");
  const [RandTeam, setRandTeam] = useState();
  const bestPokemonID = [];

  useEffect(() => {
    // This code will run after bestPokemonData has been updated
    const div = document.getElementById("10");
    const button = document.getElementById('9');
    button.style.backgroundColor = '#e75c37';
    // div.textContent = bestPokemonName;
  }, [bestPokemonName]);  

  /**
   * Function to handle fetching and setting random team data.
   */
  async function handleTeamDataRandom() {
    try {
      const result = await getRandomData();
      setRandTeam(result);
    } catch (error) {
      console.error('Error fetching data in App.js:', error);
    }
  }

  /**
   * Function to handle fetching and processing button click for loaded team data.
   */
  async function handleTeamDataLoaded() {
    try {
      const button = document.getElementById('9');
      button.style.backgroundColor = 'green';
      const result = await handleButtonClick();

      // Getting the ID of the resulting best pokemon
      for (const element of result){
        const value = await findKeyByValue(statData, element);
        bestPokemonID.push(value);
        setBestPokemonName(result);
      }
      
    } catch (error) {
      console.error('Error in handleTeamDataLoaded:', error);
    }
    console.log("Best ID:", bestPokemonID);
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
          
          <BestPokemon label="6" ID="10"/>
        </div>
      </div>
    </div>
  );
}