Computers Database Test-suite
=============================
This a test-suite that tests CRUD operations for a sample [Computer Database application](http://computer-database.herokuapp.com/computers).

Test specs
----------
Please check complete [Specs](https://docs.google.com/spreadsheets/d/1xskKBplJmHsNRqGZuFkFHUjHWOBmY_rkWJEsfVM8hpo/edit?usp=sharing).

Quickstart
----------
To run all tests, you just need to run ./tools/run_test.sh script and like magic it will do everything for you. The script will setup virtual environment then run all tests

```
compuetrs_database_testsuite$> source ./tools/run_test.sh
```

Run a specific test
-------------------
Use ./tools/setup_env.sh to setup your virtual environment and then use nosetests to run your test

```
compuetrs_database_testsuite$> source ./tools/setup_env.sh
compuetrs_database_testsuite$> venv/bin/nosetests tests/test_create.py
```
