#!/usr/bin/node

const request = require('request');

const fetchName = function (arr, i) {
  if (i >= arr.length) {
    return;
  }
  request(arr[i], function (err, response, body) {
    if (err) {
      console.log('Error', err);
    } else {
      const data = JSON.parse(body).name;
      console.log(data);
      fetchName(arr, i + 1);
    }
  });
};

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) {
    console.log('Request failed', error);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    fetchName(characters, 0);
  }
});
