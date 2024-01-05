#!/usr/bin/node
const request = require('request');
const ID = process.argv[2];
const starWarsUri = `https://swapi-api.alx-tools.com/api/films/${ID}`;
request(starWarsUri, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
