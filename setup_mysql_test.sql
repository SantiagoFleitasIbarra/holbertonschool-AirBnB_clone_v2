-- Create a database
-- Create a user
-- Grant it all the privileges in the database "hbnb_dev_db"
-- Grant the SELECT permission to the user in the database "performance_schema"

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* to 'hbnb_test'@'localhost';