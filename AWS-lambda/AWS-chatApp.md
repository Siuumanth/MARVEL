## API gateway
1. Build a socket API here, with name socketAPI, and Route selection expression `request.body.action` : A route selection expression tells API Gateway which route to call when a client sends a message.

### **What is an API Gateway?**

An **API Gateway** is a **managed service** that acts as an **entry point** for requests going to your backend services. It sits between clients (browsers, mobile apps, other servers) and backend applications (databases, Lambda functions, microservices).

It handles:
- **Routing** requests to the correct backend service.
- **Security** (authentication, authorization, rate limiting).
- **Request transformation** (modifying headers, query parameters, etc.).
- **WebSockets management** (for real-time communication).
- **Caching** to improve performance.
    
---

## **How API Gateway Works**

1️⃣ **Client makes a request** → A browser, mobile app, or another service sends a request to the API Gateway.  
2️⃣ **API Gateway processes the request** → It checks security rules, logs the request, and determines where to send it.  
3️⃣ **Routes the request to the correct backend** → Could be:
- **Lambda Function** (Serverless backend)
- **EC2 Instance** (Virtual Machine backend)
- **Containerized Service (ECS, EKS, Fargate)**
- **Database query** 4️⃣ **Backend processes and returns data** → The response goes back to the client.
#### 1.Route selection expressions

API Gateway uses the route selection expression to determine which route to invoke when a client sends a message.

When your API receives a JSON message from a client, API Gateway evaluates the route selection expression and selects the route that matches the result.

2. Then we come to API routes page, where we setup when our function should execute, eg - when a client sends a message., we get connection route, disconnect route, route key.
- The `$connect route` is triggered when a client connects to your API.
- The `$disconnect route` is triggered when either the server or the client closes the connection.
- The `$default route` is triggered if the route selection expression can't be evaluated against the message or if no matching route is found. This is the main functionality handling the request.


### 2. Attaching integrations.
Here , we set up 3 lambda functions, one for connect, one for disconnect and other for default, whenever an event occurs , these are triggered separately to make sure the job is done.

Recap:
- **Connect** – When a user joins.
- **Disconnect** – When they leave.
- **Default (Message Handler)** – To process and relay messages.
We will create 3 lambda functions for these, and add it to attach integrations, connectLambda, disconnectLambda and defaultLambda.

3. stage name - production
4.  Deploy in production stage

### **How AWS API Gateway WebSocket Works with Lambda Functions**

Yes, AWS API Gateway provides a **WebSocket endpoint** that your frontend connects to (`wss://...`). AWS also provides a way to handle WebSocket events using **Lambda functions**.

When you use `ws.connect()`, `ws.close()`, or send messages, AWS triggers **specific Lambda functions**:

|**WebSocket Action**|**Triggered Event**|**AWS API Gateway Default Lambda Function**|
|---|---|---|
|`ws = new WebSocket(url)` (Connect)|`$connect`|Handles new connections|
|`ws.send(jsonmsg)` (Send Message)|Custom action (e.g., `sendMessage`)|Processes messages|
|`ws.close()` (Disconnect)|`$disconnect`|Handles disconnections|


## Actually building the app:

## server.js:
```js
const express = require("express");
const path = require("path");
const app = express();
const PORT = 8080;

// Serve static files from the 'static' directory
app.use(express.static(path.join(__dirname, "static")));
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

## index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat APP</title>
</head>
<body>
    <h1> Chat maadi</h1>
    <div id = "status"></div>
    <input type = "text" id = "messageInput" placeholder = "Message maadu">
    <button id = "open-button">Open Connection</button>
    <button id = "send-button">Send</button>
    <button id = "close-button">Close Connection</button>
    <script src = "chat.js"></script>
</body>
</html>
```


## chat.js

This code handles the WebSocket connection; it communicates with the `API Gateway` in AWS, which manages WebSocket connections and routes messages to the appropriate Lambda functions.
```js
var ws;
function connect(){
    var url = 'wss://55uuoxgho2.execute-api.eu-north-1.amazonaws.com/production/'
    ws = new WebSocket(url)
    // instance of web socket
    //establishing connection
    ws.onopen = function(){
        console.log("connected")
        document.getElementById("status").innerHTML = "Connected";
    }
    ws.onmessage = function(event){
        //Converts (JSON) string into an object.
        var message = JSON.parse(event.data);
        console.log(message)
    }
    ws.onclose = function(){
        console.log("disconnected")
        document.getElementById("status").innerHTML = "Disconnected";
        ws = null;
    }
}

//checks if the connection is already open or not
document.getElementById("open-button").addEventListener("click", function(){
    if(ws==null){
        connect();
    }else{
        document.getElementById("status").innerHTML = "Connection is already open";
    }
});

//Send button
document.getElementById("send-button").addEventListener("click", function(){
    var message = document.getElementById("messageInput").value;
    jsonmsg = JSON.stringify({
        actionn: 'sendMessage',
        data: message
    });
    ws.send(jsonmsg);
    document.getElementById("status").innerHTML = `Message sent: ${message}`;
    alert(`Message sent: ${jsonmsg}`);
});

document.getElementById("close-button").addEventListener("click", function(){
    if(ws != null){
        ws.close();
        document.getElementById("status").innerHTML = "Connection closed";
    }
    else{
        document.getElementById("status").innerHTML = "Connection is already closed";
    }
});
```

When the client calls `connect()`, it establishes a WebSocket connection using the API Gateway's WebSocket URL. Once connected, the `onopen` event updates the UI and confirms the connection. Messages sent via the `send-button` are structured as JSON and transmitted to the server, where API Gateway routes them to the `$default` Lambda function. Incoming messages trigger the `onmessage` event, processing the response from AWS. The `close-button` terminates the connection, invoking the `$disconnect` Lambda function.

This setup allows **serverless, event-driven communication** using AWS services without maintaining a dedicated WebSocket server.

## **Chat GPT explanation**
### **Breaking Down Your WebSocket Chat Application**

Your setup consists of **three major components**:  
1️⃣ **Frontend (HTML + JavaScript) → Runs in the browser**  
2️⃣ **Backend (Express.js Server) → Serves static files**  
3️⃣ **AWS API Gateway (WebSocket) → Manages real-time communication**

Each part plays a role in ensuring real-time messaging works.

---

## **1️⃣ Frontend (HTML + JavaScript)**

This is the **user interface** where people can connect to WebSockets, send messages, and see connection status updates.

### **How It Works**

- The webpage has:
    - A status display (`<div id="status"></div>`) showing if connected/disconnected.
    - A text input box (`<input type="text">`) for entering messages.
    - Buttons for **opening the connection**, **sending messages**, and **closing the connection**.
        
- The JavaScript code **manages the WebSocket connection**:
    - **Opens a WebSocket connection** when the "Open Connection" button is clicked.
    - **Sends messages** to AWS API Gateway when the "Send" button is clicked.
    - **Closes the connection** when the "Close Connection" button is clicked.
        
- Messages are **formatted as JSON** before sending.
    - This is because API Gateway expects a structured format (`action` and `data`).
    - JSON makes it easier to send different types of actions in the future (like private messages, group chats, etc.).
        
- When a **message is received**, the JavaScript logs it to the console.
    
---
## **2️⃣ Backend (Express.js Server)**

This is a **simple Node.js server using Express.js** to serve the **static frontend files**.
### **How It Works**
- The Express app **runs on port 8080**.
- It **serves static files** (HTML, CSS, JS) from the `static` folder.
- When a user visits `http://localhost:8080`, the server sends them the `index.html` file.

🔹 **Why Do You Need a Server?**

- If you just open the HTML file from your system, it **won’t work** properly because WebSockets often require a proper HTTP server.
    
- Hosting on Express allows you to deploy it later on AWS (EC2, S3, etc.).
    
---

## **3️⃣ AWS API Gateway (WebSocket)**

This is **where the actual WebSocket connection happens**.
### **How It Works**

- The JavaScript **connects to a WebSocket URL** provided by AWS API Gateway.
- API Gateway **acts as a middleman** between the frontend and AWS Lambda.
- Every message sent through WebSockets is processed by a **Lambda function**.
    
### **AWS API Gateway WebSocket Actions**

1. **$connect**
    - Triggered when a user **connects** to the WebSocket.
    - Typically, a Lambda function **stores the connection ID** in a database (like DynamoDB).
        
2. **sendMessage**
    - Triggered when the frontend sends a message.
    - The Lambda function can:
        - **Send the message to another user** (using `postToConnection`).
        - **Store messages in a database**.
        - **Perform other logic** like filtering or formatting messages.
            
3. **$disconnect**
    - Triggered when a user **closes the connection**.
    - The Lambda function can **remove the connection ID** from the database.

🔹 **Why Use AWS API Gateway Instead of Direct WebSockets?**
- **Scalability**: AWS **manages multiple connections automatically**.
- **Security**: Can add authentication (JWT, API keys).
- **No need for a persistent server** (WebSockets usually require a backend server to keep connections alive).
---
### **Putting It All Together**

1️⃣ **User opens the webpage** → Express server serves the HTML.  
2️⃣ **User clicks "Open Connection"** → JavaScript connects to AWS API Gateway via WebSocket.  
3️⃣ **User sends a message** → API Gateway passes it to a Lambda function.  
4️⃣ **Lambda processes the message** → Forwards it to other connected users (or stores it).  
5️⃣ **User clicks "Close Connection"** → WebSocket disconnects.

---

### **Next Steps**
- **Add AWS Lambda function** to handle incoming messages.
- **Use DynamoDB** to store connection IDs (so messages can be routed).
- **Deploy the frontend** on **AWS S3** (for a public website).
- **Host the Express backend** on **EC2 or Elastic Beanstalk** if needed.