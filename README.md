## Console application “System of projects and contracts”

This is a Python Console application built using **Peewee** that uses a **PostgreSQL** database to store data.

## Table of Contents 
- [Features](#Features)  
- [Technology Stack](#Technology-Stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Console application](#run-the-application)
- [Copyright and License](#copyright-and-license)

## Features:

- [x] Create a contract
- [x] Confirm the contract
- [x] Complete the contract
- [x] Complete the contract
- [x] Show contracts
- [x] Add contract in project
- [x] Complete a contract in a project
- [x] Show projects

## Technology Stack:

-   Python
-   Peewee
-   PostgreSQL

## Prerequisites

Install the following prerequisites:

1. [Python](https://www.python.org/downloads/)
2. [PostgreSQL](https://www.postgresql.org/download/)
3. [Visual Studio Code](https://code.visualstudio.com/download) or [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/)

## Installation

#### 1. Create a virtual environment

From the **root** directory run:

```bash
python -m venv venv
```

#### 2. Activate the virtual environment

From the **root** directory run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

#### 3. Install required backend dependencies

From the **root** directory run:

```bash
pip install -r requirements.txt
```

#### 4. Set up a PostgreSQL database

With **PostgreSQL** up and running, in a new Terminal window run:

```bash
dropdb --if-exists system
```

Start **psql**, which is a terminal-based front-end to PostgreSQL, by running the command:

```bash
psql postgres
```

Create a new PostgreSQL database:

```sql
CREATE DATABASE system;
```

Create a new database admin user:

```sql
CREATE USER yourusername WITH SUPERUSER PASSWORD 'yourpassword';
```

To quit **psql**, run:

```bash
\q
```

#### 5. Set up backend environment variables

From the **root** directory run:

```bash
touch db_init/.env
```

The **touch** command will create the **.env** file in the **db_init** directory. This command works on Mac and Linux but not on Windows. If you are a Windows user, instead of using the command line, you can create the **.env** file manually by navigating in Visual Studio Code to the Explorer, clicking on the **db_init** directory (inside the **root** directory), and selecting the option **New File**.


Next, declare environment variables in the **.env** file. Make sure you don't use quotation marks around the strings.

```bash
DATABASE_NAME=system
DATABASE_USER=yourusername
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
```

#### 6. Run migrations

From the **root** directory run:

```bash
python migrate.py
```

#### 7. Run autocomplete database

From the **root** directory run:

```bash
python load_db.py
```

## Run the application

From the **root** directory run:

```bash
python setup.py
```

## Copyright and License

Copyright © 2023 Mazhar Uladzislau.