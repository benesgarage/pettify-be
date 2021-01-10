# Pettify BE

## Requirements

- Python 3
- pip
- virtualenv
- make

## Development set-up

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

- Create the database

```sh
make db
```

- Bring up the integrated web server

```sh
make up
```

You are ready to go! The server is available at localhost:8000!
