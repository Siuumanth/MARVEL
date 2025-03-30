const mysql = require('mysql2');


const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',       
    password: 'passwd'        
});


db.connect(err => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL.');
    
    db.query('CREATE DATABASE IF NOT EXISTS mydatabase', (err, result) => {
        if (err) throw err;
        console.log('Database created or already exists.');

        db.query('USE mydatabase', (err, result) => {
            if (err) throw err;

            // Create the table if it doesn't exist
            const createTableQuery = `
                CREATE TABLE IF NOT EXISTS drinks (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(80) NOT NULL UNIQUE,
                    \`desc\` VARCHAR(120)
                );
            `;
            db.query(createTableQuery, (err, result) => {
                if (err) throw err;
                console.log('Table created or already exists.');

                // Close the connection 
                db.end(err => {
                    if (err) throw err;
                    console.log('Database setup complete, connection closed.');
                });
            });
        });
    });
});
