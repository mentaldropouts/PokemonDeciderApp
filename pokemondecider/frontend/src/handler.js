import { useEffect, useState } from 'react'
import axios from "axios"

function Handler(props) {
 
 const randKeys = [];
 const [TeamData,SetTeamData] = useState();

 useEffect(() => {
  getData();
 }, []);

 function getData() {
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
  
    // console.log(TeamData);
  
  // Error handling
  }).catch((error) => {
     if (error.response) {
       console.log(error.response)
       console.log(error.response.status)
       console.log(error.response.headers)
       }
   })}

   // disabling button if full team is not already selected
   

   // creating button for randomizing the team
   return (
    <div >
      {/* Random Button  */}
      <p>Select a Random Team</p><button class="randomButton" onClick={getData}>Randomize</button>
    </div>
  );
}

export default Handler;