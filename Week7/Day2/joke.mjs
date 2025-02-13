// Function to get a joke from the JokeAPI
function getJoke() {
    const jokeResultDiv = document.getElementById('jokeResult');
    
    // Make the API request to JokeAPI
    axios.get('https://v2.jokeapi.dev/joke/Any?safe-mode')
        .then(response => {
            const joke = response.data;
            
            // Clear any previous jokes
            jokeResultDiv.innerHTML = '';

            // Check if the joke is a two-part joke or a single-line joke
            if (joke.type === 'single') {
                jokeResultDiv.innerHTML = `<p>${joke.joke}</p>`;
            } else if (joke.type === 'twopart') {
                jokeResultDiv.innerHTML = `<p><strong>Setup:</strong> ${joke.setup}</p>`;
                
                // Set a timer to display the punchline after 3 seconds
                setTimeout(() => {
                    jokeResultDiv.innerHTML += `<p><strong>Punchline:</strong> ${joke.delivery}</p>`;
                }, 5000); // 3000 milliseconds = 3 seconds
            }
        })
        .catch(error => {
            jokeResultDiv.innerHTML = `<p style="color: red;">Sorry, there was an error fetching the joke. Please try again later.</p>`;
            console.error('Error fetching joke:', error);
        });
}
