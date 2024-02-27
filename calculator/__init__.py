'''This page is refactored to have commands to perform the 4 operations'''
from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    '''command interface'''
    @abstractmethod
    def execute(self):
        '''method to represent action being performed'''

# Add Command
class AddCommand(Command):
    '''command for addition'''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 + self.num2

# Subtract Command
class SubtractCommand(Command):
    '''command for subtract'''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 - self.num2

# Multiply Command
class MultiplyCommand(Command):
    '''command for multiplication'''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 * self.num2

# Divide Command
class DivideCommand(Command):
    '''command for division'''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        if self.num2 == 0:
            return "Error: Division by zero"
        else:
            return self.num1 / self.num2

# Calculator
class Calculator:
    '''calculator class'''
    def run(self):
        '''to execute'''
        while True:
            print("Available commands: add, subtract, multiply, divide, exit")
            command = input("Enter command: ").strip().lower()
            if command == "exit":
                print("Exiting...")
                break

            if command not in ["add", "subtract", "multiply", "divide"]:
                print("Invalid command.")
                continue

            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if command == "add":
                result = AddCommand(x, y).execute()
            elif command == "subtract":
                result = SubtractCommand(x, y).execute()
            elif command == "multiply":
                result = MultiplyCommand(x, y).execute()
            elif command == "divide":
                result = DivideCommand(x, y).execute()

            print("Result:", result)

# Main
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
