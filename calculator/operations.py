'''Operations module'''

from decimal import Decimal

# Define the functions with type hints
def add(num1: Decimal, num2: Decimal) -> Decimal:
    '''Addition function'''
    return num1 + num2

def subtract(num1: Decimal, num2: Decimal) -> Decimal:
    '''Subtraction function'''
    return num1 - num2

def multiply(num1: Decimal, num2: Decimal) -> Decimal:
    '''Multiplication function'''
    return num1 * num2

def divide(num1: Decimal, num2: Decimal) -> Decimal:
    '''Division function'''
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2
