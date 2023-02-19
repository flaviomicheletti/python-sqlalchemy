

# Instalation

__venv:__

    python3 -m venv .venv && . .venv/bin/activate

## Install

In both environments you will need to install it only once.

    pip install mock
    pip install coverage
    pip install SQLAlchemy

    # pip install pytest-cov
    # pip install coverage
    # pip install psycopg2



    pip install requests

## Running

    python -m unittest discover -v
    python -m unittest discover -p 'test_*.py'


## Coverage

    coverage run -m unittest discover
    coverage report -m
    coverage html
