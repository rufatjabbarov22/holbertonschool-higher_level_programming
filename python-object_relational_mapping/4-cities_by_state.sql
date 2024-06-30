-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;

-- Use the database
USE hbtn_0e_4_usa;

-- Create states table
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,  -- Primary key for states
    name VARCHAR(256) NOT NULL,      -- Name of the state
    PRIMARY KEY (id)                 -- Primary key constraint
);

-- Insert data into states table
INSERT INTO states (name) VALUES
("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

-- Create cities table
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,      -- Primary key for cities
    state_id INT NOT NULL,               -- Foreign key to states table
    name VARCHAR(256) NOT NULL,          -- Name of the city
    PRIMARY KEY (id),                    -- Primary key constraint
    FOREIGN KEY (state_id) REFERENCES states(id)  -- Foreign key constraint
);

-- Insert data into cities table
INSERT INTO cities (state_id, name) VALUES
(1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore"), -- Cities in California
(2, "Page"), (2, "Phoenix"),     -- Cities in Arizona
(3, "Dallas"), (3, "Houston"), (3, "Austin"),   -- Cities in Texas
(4, "New York"),                 -- City in New York
(5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");  -- Cities in Nevada

