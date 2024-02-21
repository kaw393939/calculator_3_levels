# Project Starter

## Setup Instructions
1. Clone the repo
2. CD into the project folder
3. Create the virtual environment 
4. Activate the virtual environment (VE)
5. Install Requirements

## Test Commands
1. pytest run all tests
2. pytest tests/test_main.py <- Run just the tests in this file
3. pytest --pylint --cov <- Run Pylint and Coverage (Can be run independently)

## Current Libraries Installed
1. [Pytest - Testing Framework](https://docs.pytest.org/en/8.0.x/)
2. [Faker - Fake Data Creation](https://faker.readthedocs.io/en/master/)
3. [Pytest Coverage](https://pytest-cov.readthedocs.io/en/latest/readme.html)
4. [Pytest Pylint](https://pylint.readthedocs.io/en/stable/development_guide/contributor_guide/tests/launching_test.html)
## Adding Library
1.  Make sure you are in the correct VE, if not sure run "deactivate"
2.  Activate the VE
3.  Run pip freeze > requirements.txt