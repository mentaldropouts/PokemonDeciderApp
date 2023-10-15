import './App.css';
import  PokemonDropdown  from "./front"
// import Handler from "./handler"
function App() {

  return (
    <div className="App">
      <h1 class="header">Pokemon Decider</h1>
      <div class="dropdownCont">

          <div class="dropdownCol">
            <PokemonDropdown/><PokemonDropdown/><PokemonDropdown/>
          </div>

        
          
          <div class="dropdownCol">
            <PokemonDropdown/><PokemonDropdown/>
          </div>
        
        
      </div>
    </div>
  );
}

export default App;
