# Study Project for system architecture 
#### Service responsible for database connection configurations.
![Build Status](https://img.shields.io/github/workflow/status/unbrokenguy/sys-arch-conf-app/lint?label=linters)
* [Installation](#installation)
* [Setup](#setup)
* [Usage](#usage)
* [Related repositories](#related-repositories)
## Installation

#### Install poetry
```shell
pip install poetry
```

#### Install the project dependencies
```shell
poetry install 
```

## Setup

#### Add environments
* SECRET_KEY: Your secret key for django application.
* POSTGRES_HOST: PostgreSQL host.
* POSTGRES_USER: PostgreSQL user.
* POSTGRES_PASSWORD: PostgreSQL password.
* POSTGRES_NAME: PostgreSQL database name.
### Start current server
#### Spawn a shell within the virtual environment
```shell
poetry shell
```

#### Start server
```shell
cd src && python manage.py runserver 8001
```
Server will be available at this url  `http://localhost:8001/` or `http://127.0.0.1:8001/`
## Usage
* GET `/config/data/` - Retrieve database config for [Data Server](https://github.com/unbrokenguy/sys-arch-server). 
* GET `/config/auth/` - Retrieve database config for [Authorization Server](https://github.com/unbrokenguy/sys-arch-auth-app).
## Related repositories
1. [Data Server](https://github.com/unbrokenguy/sys-arch-server)
2. [Authorization Server](https://github.com/unbrokenguy/sys-arch-auth-app)
3. [Command line client](https://github.com/unbrokenguy/sys-arch-client)
4. [Front end]()