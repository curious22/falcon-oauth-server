# falcon-oauth-server

### Create PostgreSQL DB for local development:

1. Change user: `sudo su postgres`

2. Enter to psql: `psql`

3. Enter the commands one after another with the sign of the semicolon **;**
```
CREATE DATABASE oauth_db;
CREATE USER admin WITH PASSWORD 'admin2321';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE oauth_db TO admin;
```

### Create .env file for project variables 

1. Create .env file in root directory

2. Added into file following variables:
```
SECRET_KEY=YourSecretKey
DB_URI=dialect+driver://username:password@host:port/database
```