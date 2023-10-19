var express = require('express');

var app = express();
var path = require('path');
var flock = require('flockos');
var request = require('request');
var bodyParser = require('body-parser');

flock.appId = '726f83ef-3b8a-4da4-8079-22cd04b89fcf';
flock.appSecret = '51d53142-1528-4067-8be2-4ebca222776c';

var databaseUrl = "http://127.0.0.1:8002/"

app.use(flock.events.tokenVerifier);

app.use(bodyParser.urlencoded());
app.use(bodyParser.json());

app.post('/events', flock.events.listener);

app.get('/thanku', function (req, res) {
    res.send("Thank you for installing this app!")
})

app.get('/app_page', function(req, res){
    res.sendFile((path.join(__dirname + '/app.html')))
})

flock.events.on('app.install', function (event, callback) {
    //sending userid and password of new user to database.
    request.post(databaseUrl + 'add_user/', { 'form': { 'userId': event.userId, 'token': event.token } }, function (request, response) {
        if (response.statusCode === 200) {
            callback(null, 200)
        }
    });
});

app.post('/new_ticket/', function (req, res) {
    console.log(req.body);
    request.post(databaseUrl + 'new_ticket/', {
        'form':
        {
            'flock_team_id': req.body.flock_team_id,
            'name': req.body.name,
            'email': req.body.email,
            'contact_number': req.body.contact_number
        }
    })
        .on('data', function (data) {
            console.log(JSON.parse(data.toString()));
            let resData = JSON.parse(data.toString())

            let attachments = [
                {
                    "title": "New support ticket is opened by " + req.body.name,
                    "description": "Email Address: " + req.body.email,
                    "views":
                    {
                        "widget":
                        {
                            "src": "https://c11f8b80.ngrok.io/app_page"
                        }
                    }
                }
            ]

            let query = {
                token: resData.token,
                to: resData.default_channel,
                text: "New support ticket is opened!",
                attachments: JSON.stringify(attachments)
            };

            console.log(query);

            request.get({ url: "https://api.flock.co/v1/chat.sendMessage", qs: query }, function (err, response, body) {
                if (err) console.log(err);
                else console.log(body);
            })

        })

    res.sendStatus(200)
});

app.listen(8001);