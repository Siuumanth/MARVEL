const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',          
    password: 'passwd',         
    database: 'mydatabase' 
});

db.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL database.');
});

// Routes
app.get('/', (req, res) => {
    res.send('yenu illa illi');
});

// Get drinks
app.get('/drinks', (req, res) => {
    const query = 'SELECT * FROM drinks';
    db.query(query, (err, results) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        const output = results.map(drink => ({
            name: drink.name,
            desc: drink.desc
        }));
        res.json({ drinks: output });
    });
});

// Get a specific drink 
app.get('/drinks/:id', (req, res) => {
    const drinkId = req.params.id;
    const query = 'SELECT * FROM drinks WHERE id = ?';
    db.query(query, [drinkId], (err, results) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        if (results.length === 0) {
            return res.status(404).json({ error: 'Drink not found' });
        }
        const drink = results[0];
        res.json({ name: drink.name, desc: drink.desc });
    });
});

// adding drink
app.post('/drinks/add', (req, res) => {
    const { name, desc } = req.body;
    const query = 'INSERT INTO drinks (name, `desc`) VALUES (?, ?)';

    db.query(query, [name, desc], (err, result) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json({ id: result.insertId });
    });
});

// Delete 
app.delete('/drinks/del/:id', (req, res) => {
    const drinkId = req.params.id;
    const query = 'DELETE FROM drinks WHERE id = ?';
    db.query(query, [drinkId], (err, result) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        if (result.affectedRows === 0) {
            return res.status(404).json({ error: 'No drink found' });
        }
        res.json({ message: 'Deletion successful' });
    });
});

// Update 
app.put('/drinks/update/:id', (req, res) => {
    const drinkId = req.params.id;
    const { name, desc } = req.body;


    if (!name || !desc) {
        return res.status(400).json({ error: 'Name and description are required' });
    }

    const query = 'UPDATE drinks SET name = ?, `desc` = ? WHERE id = ?';
    db.query(query, [name, desc, drinkId], (err, result) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        if (result.affectedRows === 0) {
            return res.status(404).json({ error: 'Drink not found' });
        }
        res.json({ message: 'Drink updated successfully' });
    });
});



app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
