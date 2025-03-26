## Code explanation:

```javascript:
const http = require("http");    // 
const express = require("express");
const path = require('path');


const { Server } = require("socket.io"); 
//which is equal to
const socketio = require("socket.io");
const Server = socketio.Server;

```

- Http module : Node js built in used to create a server that can listen to http requests.
- Express library : web framework for simplifying building server side applications and handling requests and building APIs.
- Path module : helps in working with directories and paths. 

- Socket.io : We are importing only the Server class of socket.io , enables real time bidirectional communication. 
- Server class is used to create a WebSocket server that allows bidi communication between server and clients.


```javascript:
const app=express();  // instantiating thw express library
const server = http.createServer(app);
const io = new Server(server);  
```

- app : after instantiating , we can easily define routes and handlers like  `*app.get('/route')*`

- server : creates HTTP server using the http module. *(app)* tells the program to use the express application to handle the requests, the requests are forwarded to express app for processing. Allows you to use the HTTP server to serve both the web application and integrate with socket.io for real time comm.

- io : new instance of  socket.io server which listens to connections. `new Server(server)` attaches the Socket.IO instance to the HTTP server (`server`) created earlier.


```javascript:
io.on('connection', (socket) => {
    console.log('A new user has connected',socket.id);
    socket.on('user-message',(message) => {
        io.emit('message',message); //it means that,once a message is recieved on server side, we will send it to all other clients
    });
});

```

- The `io.on` tells to make a new connection and execute the below function whenever a new client connects to the server via websocket . `socket` parameter represents the connection between the server and that particular client. It provides methods to send and receive data specifically from and to that client.

- `socket.on` listens for a `user-message` (custom name) event from the connected client. This is received from the frontend. The function takes message as formal parameter.

- `emit `:  `io.emit('message', message)` sends the received message back to all clients, including the one who sent it. The event name `'message'` is used on the client side to identify when a new message arrives.
-


```javascript:
app.use(express.static(path.resolve("./public")));
app.get('/', (req,res) => {  
return res.sendFile('./public/index.html'); 
});
```

- These lines set up the Express application to serve static files and define a route for the root URL (`/`).

`app.use(express.static(path.resolve("./public")));`
- This line configures Express to serve **static files(frontend)** from the `./public` directory.
- **`express.static()`**: This is a built-in middleware function in Express that serves static files (like HTML, CSS, JavaScript, images, etc.). This is the function responsible for sending HTML files to the browser.
- **`path.resolve("./public")`**:  This resolves the path to the `public` directory relative to the current directory where the server is running.


`app.get('/', (req, res) => { return res.sendFile('./public/index.html'); });`

- This line defines a **route** for the root URL (`/`) of the web application. It listens to get requests  made to the root path ( / ). 
- `req` and `res` are shorthand for **request** and **response** objects in Express. They are passed as arguments to route handler functions and allow you to interact with the incoming HTTP request and send back an appropriate response.

- **`res.sendFile('./public/index.html');`**:
- This sends the `index.html` file located in the `public` directory as the response when someone accesses the root URL.
- However, to ensure compatibility, it’s recommended to use an absolute path rather than a relative one when using `res.sendFile()`. The code can be improved like this:


```javascript:
server.listen(9002, () => console.log('Server started at 9002'));
```

- This tells the HTTP server to start listening on port `9002`.
- Port `9002` is where the server will receive incoming HTTP (and WebSocket) requests.


















```javascript:
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
```