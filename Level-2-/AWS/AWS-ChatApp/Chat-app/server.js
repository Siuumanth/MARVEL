const express = require("express");
const path = require("path");
const app = express();
const PORT = 8080;

// Serve static files from the 'static' directory
app.use(express.static(path.join(__dirname, "static")));
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});