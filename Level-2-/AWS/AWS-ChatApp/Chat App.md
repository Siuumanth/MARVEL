## Adding routes:
1. connect
2. disconnect
3. default
Custom routes:
4. setName - users can set their name 
5. sendPublic - Users can send a public message
6. sendPrivate - users can send private messages

## Adding lambda functions for each route:

We will be using only 1 lambda function for each route - which is the `chat-api-handler` we will define separate functions in this.

After all that, we will get our **WebSocket URL** and **Connection URL**. The **WebSocket URL** is used by clients to establish a persistent WebSocket connection with our API Gateway. The **Connection URL** is used to send messages to a specific connection using the Connection ID.

### How This Works:

1. **Client Connects:**
    - The client establishes a WebSocket connection using the WebSocket URL.
    - API Gateway assigns a unique **Connection ID** to the client.
    - This **Connection ID** is sent to the backend Lambda function in the `$connect` route.
        
2. **Handling Messages:**
    - When a message is sent from the client, API Gateway triggers the Lambda function associated with the `$default` or other custom routes.
    - The Lambda function can process the message and decide to respond or broadcast it.
        
3. **Sending Messages to a Specific Client:**
    - API Gateway provides a **Connection URL**, which follows this format:
        `https://{api-id}.execute-api.{region}.amazonaws.com/{stage}/@connections/{connectionId}`
        
    - The backend can use this URL (with the Connection ID) to send messages to specific clients by making an HTTP POST request.
    - This is useful for implementing **private messaging, notifications, or one-to-one communication**.
        
4. **Disconnecting Clients:**
    - When a client disconnects, the `$disconnect` route is triggered.
    - The backend can remove the Connection ID from any tracking system (like DynamoDB).
### Connection ID:
- Every connected client gets a **unique Connection ID** from API Gateway.
- This Connection ID is required to send messages to a specific client.
- The backend can store these IDs in a database (e.g., DynamoDB) to manage active connections.
    
This setup allows **real-time, bidirectional communication** using a single Lambda function handling all WebSocket events efficiently.

## Building it:

Write the code in index.js for handling connections, send private and send public.

Then configure permissions, go to Configuration to allow permission for the function to work with thee API gateway execution API.
- Click on role, it will take u to IAM.
	- Add new policy - `ApiGatewayInvokeFullAccess`
Now deploy your code.