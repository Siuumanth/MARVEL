const http = require("http");
const express = require("express");
const path = require('path');

const { Server } = require("socket.io");

const app=express();
const server = http.createServer(app);
const io = new Server(server);  

// express js handles all the http requests
//below we will handle all the socket stuff

io.on('connection', (socket) => {
    console.log('A new user has connected',socket.id);

    socket.on('user-message',(message) => {
        io.emit('message',message); //it means that,once a message is recieved on server side, we will send it to all other clients
    });
});

app.use(express.static(path.resolve("./public")));


app.get('/', (req,res) => {
    return res.sendFile('./public/index.html');
}); 

server.listen(9002, () => console.log('Server started at 9002'));






