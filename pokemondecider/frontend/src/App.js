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

      <h1 class="header">Pokemon Decider</h1>
      
          <div class="dropdownBack">

            <PokemonDropdown/> <PokemonDropdown/> <PokemonDropdown/> <PokemonDropdown/> <PokemonDropdown/>

          </div>
          <div class="bestPokemon">
            <PokemonDropdown/>
          </div>

          <div class="buttonRow">
          {/* // Gives us access to the random team data */}
          <Handler onTeamDataLoaded={handleTeamDataLoaded}/>
          </div>

    </div>
  );
}

export default App;
