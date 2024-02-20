import pytest
from faker import Faker
from calculator.calculator import Calculator  

@pytest.fixture
def faker():
    return Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, help="Number of records to generate")

@pytest.fixture
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture
def generate_test_data(faker, num_records):
    test_data = []
    for _ in range(num_records):
        a = faker.random_number()
        b = faker.random_number()
        operation = faker.random_element(elements=("add", "subtract", "multiply", "divide"))
        if operation == "add":
            expected_result = a + b
        elif operation == "subtract":
            expected_result = a - b
        elif operation == "multiply":
            expected_result = a * b
        elif operation == "divide":
            expected_result = a / b if b != 0 else None
        else:
            raise ValueError("Invalid operation")
        test_data.append((a, b, operation, expected_result))
    return test_data
