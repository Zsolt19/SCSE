function getWeather() {

    const apiKey = '2b767bae393ae7e90bc4843aff5ee515';
    const city = document.getElementById('cityInput').value;  // Replace with the desired city name
    if (!city) {
        alert("Please enter a city name.");
        return;
    }
  
  
    // Make the API request
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
  
      .then(response => response.json())
      .then(data => {
        console.log("Weather Data:", data);
        // I have provided these variables for you
        const temperature = data.main.temp;
        const description = data.weather[0].description;
        const humidity = data.main.humidity;
        const windSpeed = data.wind.speed;
        // Use these to update the HTML with weather information
        const weatherResult = document.getElementById('weatherResult');
        weatherResult.innerHTML = `
            <h2>Weather in ${city}:</h2>
            <p><strong>Description:</strong> ${description}</p>
            <p><strong>Temperature:</strong> ${temperature} °C</p>
            <p><strong>Humidity:</strong> ${humidity}%</p>
            <p><strong>Wind Speed:</strong> ${windSpeed} m/s</p>          
        `;
        // Code goes here
  
      })
      .catch(error => {
        console.error('Error fetching weather data:', error); //REturns the HTTP status code
        weatherInfoElement.innerHTML = '<p>Error fetching weather data</p>';
      });
  };
  
  // Additional challenge!
  // Add functionality similar to the color picker.
  // Create a button that allows the user to enter the name of a city
  // The webpage should update with the new API information