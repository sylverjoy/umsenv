-- Create a user and grant permissions
-- CREATE USER posgress WITH PASSWORD '123456';
ALTER ROLE posgress SET client_encoding TO 'utf8';
ALTER ROLE posgress SET default_transaction_isolation TO 'read committed';
ALTER ROLE posgress SET timezone TO 'UTC';

-- Create the database and grant privileges
-- CREATE DATABASE demo6;
GRANT ALL PRIVILEGES ON DATABASE demo6 TO posgress;
