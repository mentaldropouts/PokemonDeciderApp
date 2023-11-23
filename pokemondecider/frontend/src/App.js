import './App.css';
import  PokemonDropdown  from "./front"
import Handler from "./handler"
import { useState } from'react';


function App() {

  const [RandTeam,SetRandTeam] = useState();

  const [p1,setP1] = useState("")
  const [p2,setP2] = useState("")
  const [p3,setP3] = useState("")
  const [p4,setP4] = useState("")
  const [p5,setP5] = useState("")


  const [SelectedTeam, SetSelectedTeam] = useState({
    p1: "",
    p2: "",
    p3: "",
    p4: "",
    p5: ""
  });

  // Define a function to receive the data from Handler
  const handleTeamDataLoaded = (data) => {
  SetRandTeam(data);
  console.log(RandTeam);
  };

  const handleDataP1 = (childData) => {
    console.log("Handling P1")
    setP1(childData);
  };

  return (

    <div className="App">

      <h1 class="header">Pokemon Decider</h1>
      
          <div class="dropdownBack">

            <PokemonDropdown onDataToParent={handleDataP1}/> <PokemonDropdown/> <PokemonDropdown/> <PokemonDropdown/> <PokemonDropdown/>

          </div>

          <div class="buttonRow">
          {/* // Gives us access to the random team data */}
          <Handler onTeamDataLoaded={handleTeamDataLoaded}/>
          </div>

    </div>
  );
}

export default App;
