## API gateway
1. Build a socket API here, with name socketAPI, and Route selection expression `request.body.action` : A route selection expression tells API Gateway which route to call when a client sends a message.
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


## Actually building the app