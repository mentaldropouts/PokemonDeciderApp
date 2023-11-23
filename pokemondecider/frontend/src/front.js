import { useState, useEffect } from 'react'
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

    const [selectedImage, setSelectedImage] = useState("")

    const [shortedName, setShortenedName] = useState(selectedPokemon)

    // handles dropdown operations
    const handleSlottingData = (event) => {

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

      setSelectedType1(typeData[ID][0])

      setSelectedType2(typeData[ID][1])

    };


      // Shartending the name of the pokemon to be displayed
      const handleDataChange = (event) => {

        handleSlottingData(event);
        
        const words = selectedPokemon.split(' ')
        console.log(words)
      };

    

    // Defines the teammate number above the dropdown column
    let pkmnCounter = 0;

    useEffect(() => {

      if (selectedID) {

        // Generate the image path based on the selectedID
        const imagePath = `pkmnSprites/pkmn${selectedID}.png`;

        setSelectedImage(imagePath);

        console.log(imagePath);

      } else {

        //This is when MissingNo is selected and there is no image
        setSelectedImage(""); 

      }

    }, [selectedID])

    return (

        <div class="dropdown">

        {/* <div>Pokemon {pkmnCounter}</div> */}

        <label htmlFor="pokemonSelect"></label>

        {/* Select menu for selecting any of the imported pokemon */}
        <select id="pokemonSelect" onChange={handleDataChange} value={selectedPokemon}>

          <option value="">{selectedPokemon}</option>

          {Object.keys(statData).map((id) => (

            // Putting the ID with the name so we can pull other info
            <option key={id} value={id}>

              {statData[id].Name}

            </option>

          ))}

        </select>
            
        <div class="imageContainer">

            <img class="image" src={selectedImage} alt={selectedPokemon} />
            <div class="name"> {selectedPokemon}</div>
            
        </div>

        {/* Stats for pokem */}

        {selectedPokemon && (

          <div>

            {/* <div>Selected Pokemon: {selectedPokemon} </div> */}

            {/* <div>ID: {selectedID}</div> */}

            <div class="statsholder">

              <div class="col">

              <div class="statsGrouper"> Attack <div class="stats">{selectedAttack}</div></div>

                <div class="statsGrouper"> Defense <div class="stats">{selectedDef}</div></div>

               <div class="statsGrouper"> Total <div class="stats">{selectedTotal}</div></div>

              </div>

              <div class="col">
                
                <div class="statsGrouper"> SpAtk <div class="stats">{selectedSpA}</div> </div>

                <div class="statsGrouper"> SpDef <div class="stats">{selectedDef}</div></div>

                <div class="statsGrouper"> Speed <div class="stats">{selectedSpeed}</div></div>

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