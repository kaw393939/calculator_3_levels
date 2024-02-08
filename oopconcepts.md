## Concepts and Principles in Object-Oriented Programming

### SOLID Principles

- **Single Responsibility Principle (SRP):** A class should have only one reason to change, meaning it should have only one job or responsibility.
- **Open/Closed Principle (OCP):** Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
- **Liskov Substitution Principle (LSP):** Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
- **Interface Segregation Principle (ISP):** No client should be forced to depend on methods it does not use.
- **Dependency Inversion Principle (DIP):** High-level modules should not depend on low-level modules. Both should depend on abstractions, not on concretions.

### DRY Principle

- **Don't Repeat Yourself (DRY):** This principle is about reducing the repetition of software patterns, abstracting out common functionality to prevent code duplication.

### GRASP Principles

- **General Responsibility Assignment Software Patterns (GRASP):** Guidelines for assigning responsibilities to classes and objects in OOP, like the Creator pattern which suggests a class should be responsible for creating instances of classes that it contains or closely uses.

### Separation of Concerns

- This principle involves separating a computer program into distinct sections, such that each section addresses a separate concern.

### Principles of Object-Oriented Programming

1. **Encapsulation:** Bundling of data with the methods that operate on that data.
2. **Inheritance:** A mechanism to derive a class from another class for a hierarchy of classes that share a set of attributes and methods.
3. **Abstraction:** Hiding the complex reality while exposing only the necessary parts.
4. **Polymorphism:** The ability of different classes to respond to the same message in different ways.

## Python Code Example: Calculator

```python
class Operation:
    """Base class for operations, utilizing polymorphism for extendability."""
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

class Calculation:
    """Encapsulates a single calculation."""
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def compute(self):
        """Executes the calculation."""
        return self.operation(self.a, self.b)

class CalculationsHistory:
    """Manages a history of calculations."""
    history = []
    
    @classmethod
    def add_history(cls, calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        return cls.history

class Calculator:
    """Integrates components to perform calculations and manage history."""
    def __init__(self):
        self.operations = Operation()

    def perform_calculation(self, a, b, operation):
        calculation = Calculation(a, b, operation)
        result = calculation.compute()
        CalculationsHistory.add_history(calculation)
        return result

    def get_calculation_history(self):
        return CalculationsHistory.get_history()

# Example usage
calculator = Calculator()
print(calculator.perform_calculation(10, 5, Operation.add))
print(calculator.perform_calculation(10, 5, Operation.subtract))
print(calculator.get_calculation_history())  # Display history
