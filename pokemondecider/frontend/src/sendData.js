import axios from "axios"

const sendDataToBackend = async (data) => {
    try {

      console.log("DATA: ", data);
      // Adding the labels to the payload
      const response = await axios.post('http://localhost:5000/PokeData', data);
      console.log('Data sent successfully');
      // Handle success, if needed
    } catch (error) {
      console.error('Error sending data:', error);
      // Handle error, if needed
    }
  };


  export default sendDataToBackend;