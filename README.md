# py_ip_discover

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/81fa2f6876b544b9b521fef25590d0e6)](https://www.codacy.com/gh/kevyder/py_ip_discover/dashboard) [![Build Status](https://travis-ci.com/kevyder/py_ip_discover.svg?branch=master)](https://travis-ci.org/kevyder/py_ip_discover) [![Coverage Status](https://coveralls.io/repos/github/kevyder/py_ip_discover/badge.svg?branch=master)](https://coveralls.io/github/kevyder/py_ip_discover?branch=master)

This project was generated via [manage-fastapi](https://ycd.github.io/manage-fastapi/)! :tada:

## Usage

You need to create a .env file in the root directory of the project:

```

PROJECT_NAME=py_ip_discover
BACKEND_CORS_ORIGINS=["http://localhost:8000", "https://localhost:8000", "http://localhost", "https://localhost"]


POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=database
POSTGRES_DB=ip_discover


IP_GEOLOCATION_URL="http://ip-api.com/json"
CURRENCY_CONVERTER_URL = "https://api.apilayer.com/fixer/latest"
CURRENCY_CONVERTER_APIKEY = "YOUR_APIKEY"

```

Build the Docker image

```bash
docker-compose build
```

Run application

```bash
docker-compose up
```

Run Tests

```bash
docker-compose run --rm app coverage run -m pytest
```

Get tests coverage

```bash
docker-compose run --rm app coverage report
```

### Documentation

Access swagger at: http://127.0.0.1:8000/docs

## License

This project is licensed under the terms of the Apache license.
