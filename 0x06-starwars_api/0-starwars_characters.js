#!/usr/bin/node

// Import necessary packages
const request = require('request');

// Check if a Movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: ./starWarsCharacters.js <Movie ID>');
  process.exit(1);
}

// Get the Movie ID from command-line arguments
const movieId = process.argv[2];

// Define the URL to fetch movie data from the Star Wars API
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a GET request to the API
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusMessage);
    process.exit(1);
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Extract and print character names
  movieData.characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        process.exit(1);
      }

      if (charResponse.statusCode !== 200) {
        console.error('Error:', charResponse.statusMessage);
        process.exit(1);
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
