-- Create a database
-- Create a user
-- Grant it all the privileges in the database "hbnb_dev_db"
-- Grant the SELECT permission to the user in the database "performance_schema"

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';