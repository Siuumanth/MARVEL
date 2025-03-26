const express = require("express");
const path = require("path");

const app = express();
const port = 3000;

// Serve static files from the current directory
app.use(express.static(__dirname));

// Handle all requests
app.get("*", (req, res) => {
    const filePath = path.join(__dirname, req.path === "/" ? "index.html" : req.path + ".html");

    res.sendFile(filePath, (err) => {
        if (err) {
            res.status(404).send("404 : File not FOUND MACHA");
        }
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
