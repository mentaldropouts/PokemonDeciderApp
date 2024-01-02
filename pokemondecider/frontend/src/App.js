import './App.css';
// import ReactDOM from 'react-dom/client';
import { createRoot } from 'react-dom/client';
import  PokemonDropdown  from "./front"
// import GetBestInfo from './getBestInfo'
import handleButtonClick from './sendButton'
import { statData } from './Stats';
import getRandomData from './sendRandTeam';
import { useState, useEffect } from'react'
import BestPokemon from './frontBest';


function App() {
  let bestPokemonArray = [];
  const [ElementsCreated,setElementsCreated] = useState(false);
  const [RandTeam, setRandTeam] = useState();

  useEffect(() => {
    const submitButton = document.getElementById('submitButton');
    submitButton.style.backgroundColor = '#e75c37';
    if (ElementsCreated.length > 0){
      submitButton.style.backgroundColor = 'blue';
      const elementContainer = document.createElement('elementContainer');
      clearElements(elementContainer);
    }
}, [bestPokemonArray]);  


function createElementsAsync(){
  const elementContainer = document.getElementById('elementContainer');
  const root = createRoot(elementContainer);
  return new Promise((resolve, reject) => {
    console.log("Number of elements to create: ", bestPokemonArray.length);
    const numberOfElements = bestPokemonArray.length;
    for (let i = 1; i <= numberOfElements; i++) {
        // console.log("DATA: ", bestPokemonArray[i - 1]);
        // console.log("Name: ", bestPokemonArray[i - 1]['name']);
        // console.log("ID: ", bestPokemonArray[i - 1]['id']);
        // console.log("Image: ", bestPokemonArray[i - 1]['image']);
        // const key = `bestPokemon_${i}`;
        const { name, id, image } = bestPokemonArray[i - 1];
          
          root.render(
            <BestPokemon
              dataName={name}
              dataNumber={id}
              dataPicture={image}
            />

          
        );
    }
    setElementsCreated(true);
    // Resolve the promise to indicate success
    resolve();
  });
}


function clearElements(elementContainer){
  // Remove all child elements from the container
  while (elementContainer.firstChild) {
      elementContainer.removeChild(elementContainer.firstChild);
  }
  setElementsCreated(false);
}

// Finding a key in a statData by the name of the pokemon.
async function findKeyByValue(obj, value) {
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
    bestPokemonArray = [];
    try {
      const result = await  getRandomData();
      setRandTeam(result)
      } catch (error) {
        console.error('Error fetching data in App.js:', error);
      }
  }

  async function handleTeamDataLoaded() {
    try {
      const button = document.getElementById('submitButton');
      button.style.backgroundColor = 'green';
      const result = await handleButtonClick();
      console.log("RESULT from handleButtonClick: ", result);
      button.style.backgroundColor = '#e75c37';
      await processResultElements(result);
      // Making Best Pokemon Blocks dynamicly
      
    } catch (error) {
      console.error('Error in handleTeamDataLoaded:', error);
    }
  }
  
  async function processResultElements(elements) {
    for (const element of elements) {
      try {
        console.log("Processing element:", element);
        const value = await findKeyByValue(statData, element);
        console.log("VALUE:", value);
        bestPokemonArray.push({
          name: statData[value]["Name"],
          id: statData[value]["ID"],
          image: `pkmnSprites/pkmn${statData[value]["ID"]}.png`
        });
        console.log("BEST POKEMON ARRAY:", bestPokemonArray);
        createElementsAsync();
      } catch (error) {
        console.error("Error processing element:", error);
      }
    }
  }
  

  return (
    <div className="App">
      <h1 class="header">Pokemon Decider</h1>
    
          <div class="dropdownBack">
            <PokemonDropdown label="1" Data={RandTeam}/> 
            <PokemonDropdown label="2" Data={RandTeam}/> 
            <PokemonDropdown label="3" Data={RandTeam}/> 
            <PokemonDropdown label="4" Data={RandTeam}/> 
            <PokemonDropdown label="5" Data={RandTeam}/>
          </div>

          <div class="bestPokemon">
            <div class="buttonRow">
              <button class="Button" id ="8" onClick={handleTeamDataRandom}>Random</button>
              <button class="Button" id ="submitButton" data={bestPokemonArray} onClick={handleTeamDataLoaded}>Submit</button>
            </div>
            <div id="elementContainer"></div>
        </div>
    </div>
  );
}

export default App;
