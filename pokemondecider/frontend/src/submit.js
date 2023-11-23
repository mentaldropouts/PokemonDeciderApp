import { useEffect, useState } from 'react'
import axios from "axios"

const sendDataToBackend = async (data) => {
    try {
      const response = await axios.post('/submit', data);

      console.log('Data sent successfully');
      // Handle success, if needed
    } catch (error) {
      console.error('Error sending data:', error);
      // Handle error, if needed
    }
  };

  export default sendDataToBackend;