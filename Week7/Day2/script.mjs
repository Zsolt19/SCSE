// cimport axios from 'axios'
axios.get('https://v2.jokeapi.dev/joke/Any?safe-mode')

  .then(function(response) {
    console.log(response.data) // Access the response data
  })

  .catch(function(error) {
    console.log(error) // error handling, this code executes if the request is denied
  })

  .finally(function() {
    console.log("Code has finished executing.") // This code ALWAYS executes
  })