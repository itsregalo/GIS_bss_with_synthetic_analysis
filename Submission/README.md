# Setting up the environment

## Install dependencies

```bash
pip install -r requirements.txt
```

## Create database

* Databaseused is PostgreSQL with postgis extension

```bash
sudo apt install postgresql postgresql-contrib
```

```bash
sudo systemctl start postgresql.service
```

```bash
sudo -i -u postgres
```

```bash
psql
```

```sql
-- set password for postgres user

\password postgres
```

```sql
-- create database

CREATE DATABASE <database_name>;
```

```sql
-- create extension postgis

CREATE EXTENSION postgis;
```

## Create .env file

* Create a .env file in the root directory of the project

```bash
touch .env
```

* Add the following to the .env file

```bash
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
```

* Replace the following with your own values

* username
* password
* database_name

## Run migrations

```bash
python manage.py migrate
```

## Create superuser

```bash
python manage.py createsuperuser
```

## Run server

```bash
python manage.py runserver
```
