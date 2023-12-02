import { useEffect, useState } from 'react'
import axios from "axios"
import handleButtonClick from './sendButton'


function Handler(props) {
 const randKeys = [];
 const [TeamData,SetTeamData] = useState();

 useEffect(() => {
  getRandomData();
 }, []);

 function getRandomData() {
   axios({
     method: "GET",
     url:"/test",
   })

   // Catching the data from the backend
   .then((response) => {
     const res = response.data
     const keys = Object.keys(res)
     const data = keys.map(key => res[key]);

    // If data then Set it to const
    if (data){
      SetTeamData(TeamData);
      props.onTeamDataLoaded(data);
    }
  
    console.log(TeamData);
  
  // Error handling
  }).catch((error) => {
     if (error.response) {
       console.log(error.response)
       console.log(error.response.status)
       console.log(error.response.headers)
       }
   })}

   // creating button for randomizing the team
   return (

    <div >
    
      {/* Random Button  */}
      <button class="Button" onClick={getRandomData}>Randomize</button>
      
      {/* Submit Button  ( DOESNT HAVE A BINDING YET ) */} 
      
      {/* <button class="Button" onClick={handleButtonClick}> Submit</button> */}

      {/* <button class="Button" onClick={submitTeam}>Submit</button> */}


    </div>
  );
}

export default Handler;