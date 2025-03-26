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