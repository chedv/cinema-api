# Local development

Install pipenv:

```shell script
python3.8 -m pip install pipenv
```

Clone project:

```shell script
git clone https://github.com/chedv/cinema-api.git
cd cinema-api
```

Configure vscode settings.json:

```json
{
    "python.pythonPath": "/path/to/project/.venv/bin/python3.8",
    "python.linting.pylintEnabled": true,
    "python.linting.pycodestyleEnabled": true
}
```

Create virtual environment and install dependencies:

```shell script
pipenv install --python 3.8
pipenv shell
```

Add .env file:

```shell script
APP_HOST=localhost
APP_PORT=8000

DB_USER=<user>
DB_PWD=<password>
DB_NAME=<name>
DB_HOST=localhost
DB_PORT=5432
DB_ECHO=true

JWT_SECRET=<key>
```

Run project:

```shell script
python3.8 main.py
```

Run tests:

```shell script
python3.8 -m pytest
```

Run coverage tool:

```shell script
python3.8 -m pytest --cov=app tests/
```