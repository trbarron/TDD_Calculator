import unittest
from calculator import *


class mock_stdin(object):
    def read_line():
        return "hmm"

class calculator_test(unittest.TestCase):

    def test_sanity(self):
        assert calculator.calculate("1+1") is not None

    def test_addition_1(self):
        self.assertEqual(calculator.calculate("1+4"),5)

    def test_addition_2(self):
        self.assertEqual(calculator.calculate("14+26"),40)

class get_input_test(unittest.TestCase):

    def test_get_one_line(self):
        assert get_input(mock_stdin) == "hmm"

class parse_input_test_get_tokens(unittest.TestCase):

    def test_addition_single_digit_1(self):
        self.assertEqual(parse_input_get_tokens("7+3"),[7,"+",3])

    def test_addition_single_digit_2(self):
        self.assertEqual(parse_input_get_tokens("2+8"),[2,"+",8])

    def test_addition_double_digit_1(self):
        self.assertEqual(parse_input_get_tokens("15+4"),[15,"+",4])

    def test_addition_double_digit_2(self):
        self.assertEqual(parse_input_get_tokens("18+90"),[18,"+",90])

class translate_tokens_to_ops_test(unittest.TestCase):

    def test_addition_tokens_1(self):
        self.assertEqual(translate_tokens_to_ops([1,"+",5]),("+",1,5))
    
    def test_addition_tokens_2(self):
        self.assertEqual(translate_tokens_to_ops([14,"+",3]),("+",14,3))

            
class evaluate_ops_test(unittest.TestCase):

    def test_evaluate_addition_op_1(self):
        self.assertEqual(evaluate_ops(("+",4,8)), 12)

    def test_evaluate_addition_op_2(self):
        self.assertEqual(evaluate_ops(("+",3,11)), 14)

if __name__ == "__main__":
    unittest.main()

