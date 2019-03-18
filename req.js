var message = "Does the switch Cisco Catalyst 9300 support IoT ?";
const deasync = require('deasync');
var http = require('http');
const querystring = require('querystring')
const axios = require('axios');
var response;

try{
    axios.post('http://10.138.89.32:8000/results/', {"input": message}, {
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
}).then(function (response) {
console.log(response.data.Answer);
})
.catch(function (error) {
console.log(error);
});

} 
catch (err) {
console.log(err);
response = "error!"
}
