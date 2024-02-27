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
        return self.num1 / self.num2

# Menu Command
class MenuCommand(Command):
    '''menu'''
    def __init__(self, command_dict):
        self.command_dict = command_dict

    def execute(self):
        print("Available commands:")
        for command_name in self.command_dict:
            print(command_name)

# Calculator
class Calculator:
    '''calculator class'''
    def __init__(self):
        self.commands = {
            "add": AddCommand,
            "subtract": SubtractCommand,
            "multiply": MultiplyCommand,
            "divide": DivideCommand,
            "menu": MenuCommand
        }

    def run(self):
        '''executing calculator commands'''
        while True:
            print("Available commands: add, subtract, multiply, divide, menu, exit")
            user_input = input("Enter command and numbers in the following format (add 5 3): ").strip().lower()

            if user_input == "exit":
                print("Exiting")
                break

            command_parts = user_input.split()
            command_name = command_parts[0]

            if command_name not in self.commands:
                print("Invalid command.")
                continue

            if command_name == "menu":
                MenuCommand(self.commands).execute()
                continue

            try:
                x = float(command_parts[1])
                y = float(command_parts[2])
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid numbers.")
                continue

            command = self.commands[command_name](x, y)
            result = command.execute()
            print("Result:", result)

# Main
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
