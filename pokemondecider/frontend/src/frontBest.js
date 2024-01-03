import { useState, useEffect } from 'react'
import './App.css';

function BestPokemon( {dataName, dataNumber, dataPicture} ) {
const [selectedPokemonData, setSelectedPokemonData] = useState({
    name: dataName,
    id: dataNumber,
    image: dataPicture
  });

  useEffect(() => {  
      console.log("Number in Best: ", selectedPokemonData.id);
      console.log("Name in Best: ", selectedPokemonData.name);
      console.log("Picture in Best: ", selectedPokemonData.image);
    }, [selectedPokemonData]);
  
  return (
        <div class="sixthholder">
          <div class='imageContainerBorder'>
            <div class="imageContainerBest">
              <img class="image" src={selectedPokemonData.image} alt={selectedPokemonData.name} />
              <div class="name1"> {selectedPokemonData.name}</div>
            </div>
          </div>
        </div>
        )};
      
  export default BestPokemon;