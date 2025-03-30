var ws;

function connect() {
    var url = 'wss://55uuoxgho2.execute-api.eu-north-1.amazonaws.com/production/';
    ws = new WebSocket(url); // instance of web socket

    // establishing connection
    ws.onopen = function () {
        console.log("connected");
        document.getElementById("status").innerHTML = "Connected";
    };

    ws.onmessage = function (event) {
        // Converts (JSON) string into an object.
        var message = JSON.parse(event.data);
        console.log(message);
    };

    ws.onclose = function () {
        console.log("disconnected");
        document.getElementById("status").innerHTML = "Disconnected";
        ws = null;
    };
}

// checks if the connection is already open or not
document.getElementById("open-button").addEventListener("click", function () {
    if (ws == null) {
        connect();
    } else {
        document.getElementById("status").innerHTML = "Connection is already open";
    }
});

// send button
document.getElementById("send-button").addEventListener("click", function () {
    var message = document.getElementById("messageInput").value;
    jsonmsg = JSON.stringify({
        actionn: 'sendMessage',
        data: message
    });
    ws.send(jsonmsg);
    document.getElementById("status").innerHTML = `Message sent: ${message}`;
    alert(`Message sent: ${jsonmsg}`);
});

document.getElementById("close-button").addEventListener("click", function () {
    if (ws != null) {
        ws.close();
        document.getElementById("status").innerHTML = "Connection closed";
    } else {
        document.getElementById("status").innerHTML = "Connection is already closed";
    }
});
