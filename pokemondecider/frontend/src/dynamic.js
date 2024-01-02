document.addEventListener('DOMContentLoaded', function() {
    const submitButton = document.getElementById('submitButton');
    const elementContainer = document.getElementById('elementContainer');
    let elementsCreated = false;

    submitButton.addEventListener('click', ( ) => {
        if (elementsCreated) {
            clearElements();
        } else {
            createElementsAsync();
        }
    });

    function createElementsAsync() {
        return new Promise((resolve, reject) => {
            submitButton.style.backgroundColor = 'blue';
            console.log("Number of elements to create: ", submitButton.data.length);
            const numberOfElements = submitButton.data.length;
            for (let i = 1; i <= numberOfElements; i++) {
                const newElement = document.createElement('div');
                newElement.textContent = `Element ${i}`;
                elementContainer.appendChild(newElement);
            }
            elementsCreated = true;
            // Resolve the promise to indicate success
            resolve();
        });
    }
    
    // Example of using the asynchronous createElements function
    createElementsAsync()
        .then(() => {
            console.log('Elements created successfully!');
            // Perform actions after elements are created
        })
        .catch((error) => {
            console.error('Error creating elements:', error);
            // Handle errors if needed
    });


    function clearElements() {
        // Remove all child elements from the container
        while (elementContainer.firstChild) {
            elementContainer.removeChild(elementContainer.firstChild);
        }
    
        elementsCreated = false;
    }
});



