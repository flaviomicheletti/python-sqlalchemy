# Python SQLAlchemy Unittest

![image](https://user-images.githubusercontent.com/1257048/219973971-906c02d6-3ca9-489d-9aed-ce38d1b466b4.png)


__venv:__

    python3 -m venv .venv && . .venv/bin/activate

    pip install mock
    pip install coverage
    pip install SQLAlchemy

    # pip install pytest-cov
    # pip install coverage
    # pip install psycopg2

__Running:__

    python -m unittest discover -v

    python -m unittest discover example01/

__Coverage:__

    coverage run -m unittest discover
    coverage report -m
    coverage html

    coverage run -m unittest discover && coverage report -m && coverage html

## Articles

- [SQLAlchemy-Utils](https://sqlalchemy-utils.readthedocs.io/)


## Drafts

```python
import logging
logging.disable(logging.WARNING)
```

```python
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDatabase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    assert result.wasSuccessful() and result.coverage == 100
```