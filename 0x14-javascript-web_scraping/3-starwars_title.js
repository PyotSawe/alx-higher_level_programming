#!/usr/bin/node
const request = require('request');
const ID = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request(endPoint, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
