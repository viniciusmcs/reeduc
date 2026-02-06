-- Create PostgreSQL role and database for REEDUC
-- Execute with a superuser (e.g., postgres)

CREATE USER sejus WITH PASSWORD 'sejus@pi';
CREATE DATABASE reeducdb OWNER sejus;
GRANT ALL PRIVILEGES ON DATABASE reeducdb TO sejus;
