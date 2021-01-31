# Pettify BE

## Set-up

This project makes use of docker, but also supports standalone deployment. Please see each relevant section for details

### Standalone set-up

#### Requirements

- Python 3
- pip
- virtualenv
- make

#### Steps

- Install python 3, pip & virtualenv
- Create virtual environment within the project root folder

```sh
virtualenv -p python3 venv
```

- Activate virtual environment

```sh
source venv/bin/activate
```

- Install dependencies

```sh
pip install -r requirements.txt
```

- Run the following to use the standalone Makefile configuration

```sh
make -f Makefile.standalone configure
```

> You can switch to the docker Makefile at anytime by running `make switch`

- Create the database

```sh
make db
```

- Bring up the integrated web server

```sh
make server
```

You are ready to go! The server is available at localhost:8000!

### Docker set-up

#### Requirements

- docker
- docker-compose

#### Steps

- Run the following to use the docker Makefile configuration

```sh
make -f Makefile.docker configure
```

> You can switch to the standalone Makefile at anytime by running `make switch`

- Spin up the containers
```sh
make up
```

- Create the database

```sh
make db
```

- Bring up the integrated web server

```sh
make server
```

You are ready to go! The server is available at localhost:8000!
