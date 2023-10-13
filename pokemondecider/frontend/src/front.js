import { useState } from 'react';
import { statData } from "./Stats"
import { typeData } from "./Types"

function PokemonDropdown() {
    const [selectedPokemon, setSelectedPokemon] = useState("MissingNo."); // State to store the selected Pokemon
    const [selectedID, setSelectedID] = useState("");
    const [selectedTotal, setSelectedTotal] = useState("")
    const [selectedHP, setSelectedHP] = useState("")
    const [selectedAttack, setSelectedAttack] = useState("")
    const [selectedDef, setSelectedDef] = useState("")
    const [selectedSpA, setSelectedSpA] = useState("")
    const [selectedSpD, setSelectedSpD] = useState("")
    const [selectedSpeed, setSelectedSpeed] = useState("")  
    const [selectedType1, setSelectedType1] = useState("")
    const [selectedType2, setSelectedType2] = useState("")

    // handles dropdown operations
    const handleSelectChange = (event) => {
      const ID = event.target.value;
      console.log(ID)
      setSelectedID(ID);
      setSelectedPokemon(statData[ID].Name)
      setSelectedTotal(statData[ID].Total)
      setSelectedHP(statData[ID].HP)
      setSelectedAttack(statData[ID].Attack)
      setSelectedDef(statData[ID].Defense)
      setSelectedSpA(statData[ID].SpAtk)
      setSelectedSpD(statData[ID].SpDef)
      setSelectedSpeed(statData[ID].Speed)
      // adding type
      setSelectedType1(typeData[ID][0])
      setSelectedType2(typeData[ID][1])

    };

    return (
        <div class="dropdown">
        {/* <h1>Pokemon Dropdown</h1> */}
        <label htmlFor="pokemonSelect"></label>
        <select id="pokemonSelect" onChange={handleSelectChange} value={selectedPokemon}>
          <option value="">{selectedPokemon}</option>
          {Object.keys(statData).map((id) => (
            // Putting the ID with the name so we can pull other info
            <option key={id} value={id}>
              {statData[id].Name}
            </option>
          ))}
        </select>
        {selectedPokemon && (
          <div>
            <div>Selected Pokemon: {selectedPokemon} </div>
            <div>Total: {selectedTotal}</div>
            <div class="statsholder">
              <div class="col">
                <div>HP: {selectedHP}</div>
                <div>Attack: {selectedAttack}</div>
                <div>Defense: {selectedDef}</div>
              </div>
              <div class="col">
                <div>SpAtk: {selectedSpA}</div>
                <div>SpDef: {selectedSpD}</div>
                <div>Speed: {selectedSpeed}</div>
             </div>
              <div>

              </div>
            </div>
            <div class="typeholder">
              <div> {selectedType1} {selectedType2}</div>
              
            </div>  
          </div>
          
        )}
      </div>
    );
  }
  
  export default PokemonDropdown;