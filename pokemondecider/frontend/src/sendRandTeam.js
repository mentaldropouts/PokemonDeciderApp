import axios from "axios";

const getRandomData = async () => {
  try {
    const response = await axios({
      method: "GET",
      url: "/RandPokeData",
    });

    const res = response.data;
    // console.log("DATA: ", res)
    const keys = Object.keys(res);
    const data = keys.map((key) => res[key]);
    
    console.log("Data received in getRandomData:", data);
    return data
  } catch (error) {
    if (error.response) {
      console.error(error.response);
      console.error(error.response.status);
      console.error(error.response.headers);
    }
    throw error; // Re-throw the error to be caught in the calling code
  }
};

export default getRandomData;
