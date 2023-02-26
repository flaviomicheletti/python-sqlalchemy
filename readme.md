# Python SQLAlchemy Unittest

![image](https://user-images.githubusercontent.com/1257048/219973971-906c02d6-3ca9-489d-9aed-ce38d1b466b4.png)


## Instalation

__venv:__

    python3 -m venv .venv && . .venv/bin/activate

    pip install mock
    pip install coverage
    pip install SQLAlchemy

    # pip install pytest-cov
    # pip install coverage
    # pip install psycopg2


## Running

    python -m unittest discover -v

    python -m unittest discover example01/

## Coverage

    coverage run -m unittest discover
    coverage report -m
    coverage html

    coverage run -m unittest discover && coverage report -m && coverage html
