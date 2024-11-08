import unittest
from math_quiz import function_A, function_B, function_C

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # testing that random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Testing that a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Value {rand_num} out of range")

    def test_function_B(self):
        # Testing that if the selected operator is one of the expected operators
        operators = {'+', '-', '*'}
        for _ in range(100):  
            operator = function_B()
            self.assertIn(operator, operators, f"Unexpected operator {operator}")

    def test_function_C(self):
        # Test cases to check if the math problem and answer are generated correctly
        test_cases = [
            (5, 2, '+', '5 + 2', 7),   # Addition
            (7, 3, '-', '7 - 3', 4),   # Subtraction
            (4, 6, '*', '4 * 6', 24)   # Multiplication
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Expected problem '{expected_problem}', got '{problem}'")
            self.assertEqual(answer, expected_answer, f"Expected answer {expected_answer}, got {answer}")

if __name__ == "__main__":
    unittest.main()
