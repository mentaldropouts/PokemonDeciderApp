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

        // Parse the JSON in the response
        const data = await response.json();
        
        if (data && data.result) {
            console.log("Received in handleButtonClick: ", data.result);
            return data.result;
        } else {
            console.error('Invalid or undefined result in the response:', data);
            // Handle the error or return an appropriate value
            // For example, return an empty array or throw a new error
            return [];
        }
        
    } catch (error) {
        console.error('Fetch or parsing error:', error);
        // Handle the error or return an appropriate value
        // For example, return an empty array or throw a new error
        return [];
    }
};

export default handleButtonClick;
