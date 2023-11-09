import './App.css';
import  PokemonDropdown  from "./front"
import Handler from "./handler"
import { useState } from'react';

function App() {
  const [RandTeam,SetRandTeam] = useState();

  // Define a function to receive the data from Handler
  const handleTeamDataLoaded = (data) => {
  SetRandTeam(data);
  console.log(RandTeam);
  };

  return (
    <div className="App">
      {/* Nested header containing app name and subtitle for the app */}
      <h1 class="header">Pokemon Decider App
      <h2 class="header2">Find an ideal 6th team member for your Pokemon team</h2>
      </h1>
    
      {/* This is a container to hold info describing how the app works/how to use it */}
      <div class = "infoBox">
        <h2>How to use the app</h2>
        {/* TODO: Update this information when functionality is added! */}
        <p class ="infoBoxInternal">To use the decider app, please input your team of 5 Pokemon and submit them. 
        Our algorithms will pick the best 6th member for your team! Click the random button to recieve a random team.</p>
      </div>
      <div class="dropdownCont">

          <div class="dropdownCol">
            <PokemonDropdown/><PokemonDropdown/><PokemonDropdown/>
          </div>
      
          <div class="dropdownCol">
            <PokemonDropdown/><PokemonDropdown/>
          </div>
      
      </div>
      {/* // Gives us access to the random team data */}
      <Handler onTeamDataLoaded={handleTeamDataLoaded}/>
    </div>
  );
}

export default App;
