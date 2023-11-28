import './App.css';
import  PokemonDropdown  from "./front"
import Handler from "./handler"
import { useState } from'react';
import BestPokemon from './front2';


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

            <PokemonDropdown label="1"/> <PokemonDropdown label="2"/> <PokemonDropdown label="3"/> <PokemonDropdown label="4"/> <PokemonDropdown label="5"/>

          </div>
          <div class="bestPokemon">
            <BestPokemon/>
          </div>

          <div class="buttonRow">
          {/* // Gives us access to the random team data */}
          <Handler onTeamDataLoaded={handleTeamDataLoaded}/>
          </div>

    </div>
  );
}

export default App;
