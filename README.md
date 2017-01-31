# falcon-oauth-server

An implementation of OAuth REST API server on Falcon. Based on 
[falcon-rest-api](https://github.com/ziwon/falcon-rest-api) repository.

## Requirements

 - Python 3.5.2
 - Cerberus 1.1
 - Cython 0.25.2
 - falcon 1.1.0
 - gunicorn 19.6.0
 - itsdangerous 0.24
 - psycopg2 2.6.2
 - pytest 3.0.6
 - python-decouple 3.0
 - requests 2.13.0
 - SQLAlchemy 1.1.5


## Local deployment

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
LOG_LEVEL=DEBUG
```

### Run server

1. Type `make start-server`

2. Navigate to `http://0.0.0.0:5000/`

### Run tests

Type `pytest -v`

## Docs

API endpoints:
 - [/v1/users](docs/user's_endpoint.md)