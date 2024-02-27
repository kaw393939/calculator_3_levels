'''My Calculator Test'''
import unittest
from calculator import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class TestCalculatorCommands(unittest.TestCase):
    '''testing for calculator with commands'''
    def test_add(self):
        '''test addition'''
        add = AddCommand(5, 3)
        self.assertEqual(add.execute(), 8)

    def test_subtract(self):
        '''test subtraction'''
        subtract = SubtractCommand(5, 3)
        self.assertEqual(subtract.execute(), 2)

    def test_multiply(self):
        '''test multiplication'''
        multiply = MultiplyCommand(5, 3)
        self.assertEqual(multiply.execute(), 15)

    def test_divide(self):
        '''test division'''
        divide = DivideCommand(6, 3)
        self.assertEqual(divide.execute(), 2)

    def test_divide_by_zero(self):
        '''test for division by zero error'''
        divide_by_zero = DivideCommand(5, 0)
        self.assertEqual(divide_by_zero.execute(), "Error: Division by zero")

if __name__ == '__main__':
    unittest.main()
