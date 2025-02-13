function getWeather() {
    const apiKey = '2b767bae393ae7e90bc4843aff5ee515'; // Replace with your API key
    const city = document.getElementById('cityInput').value;

    if (!city) {
        alert("Please enter a city name.");
        return;
    }

    // Make the API request
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Weather Data:", data);

            // Extract weather information
            const temperature = data.main.temp;
            const description = data.weather[0].description;
            const weatherCondition = data.weather[0].main.toLowerCase(); // e.g., "clear", "rain", "clouds"
            const humidity = data.main.humidity;
            const windSpeed = data.wind.speed;
            const windSpeedKmh = (windSpeed * 3.6).toFixed(1); // rounded to 1 decimal place
            const city=data.name;

            // Update the HTML with weather information
            const weatherResult = document.getElementById('weatherResult');
            weatherResult.innerHTML = `
                <div class="weather-icon">${getWeatherIcon(weatherCondition)}</div>
                <h2>Weather in ${city}:</h2>
                <p><strong>Description:</strong> ${description}</p>
                <p><strong>Temperature:</strong> ${temperature} °C</p>
                <p><strong>Humidity:</strong> ${humidity}%</p>
                <p><strong>Wind Speed:</strong> ${windSpeedKmh} km/h</p>
            `;

            // Update the background based on weather condition
            document.body.className = weatherCondition;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            const weatherResult = document.getElementById('weatherResult');
            weatherResult.innerHTML = '<p style="color: red;">Error fetching weather data. Please try again.</p>';
        });
}

// Helper function to get weather icons
function getWeatherIcon(condition) {
    switch (condition) {
        case 'clear':
            return '☀️'; // Sun icon
        case 'clouds':
            return '☁️'; // Cloud icon
        case 'rain':
            return '🌧️'; // Rain icon
        case 'snow':
            return '❄️'; // Snow icon
        case 'thunderstorm':
            return '⛈️'; // Thunderstorm icon
        default:
            return '🌤️'; // Default icon
    }
}