

const handleButtonClick = async () => {
    try {
        // Send a POST request to the Flask server
        const response = await fetch('http://localhost:5000/buttonPressed', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ buttonPressed: true }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        else{

            // Parse the JSON in the response
            const data = await response.json();

            // Update the state or handle the response as needed
            console.log("Result: ",data.result[0]);
            return data.result
        }

    } catch (error) {
        console.error('Fetch error:', error);
    }
};



export default handleButtonClick;