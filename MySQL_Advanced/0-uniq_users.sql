-- Check if a table exists and create it if it does not
SET sql_notes = 0; -- Temporarily disable the "Table already exists" warning
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    CONSTRAINT email_unique UNIQUE (email)
) ENGINE=InnoDB;
SET sql_notes = 1; -- Re-enable the warning
