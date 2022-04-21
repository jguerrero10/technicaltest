import unittest
from utils import Struct


class TestStruct(unittest.TestCase):

    def test_max_number(self):
        data = [1, 2, 3, 4, 5, 6]
        arr_test = Struct(data)
        self.assertEqual(arr_test.max_number(), 6)

    def test_min_number(self):
        data = [3, 6, 8, 10, 15, 2]
        arr_test = Struct(data)
        self.assertEqual(arr_test.min_number(), 2)

    def test_first_num(self):
        data = [456, 654, 21, 2, 12]
        arr_test = Struct(data)
        self.assertEqual(arr_test.first_num(), 456)

    def test_last_num(self):
        data = [456, 654, 21, 2, 12]
        arr_test = Struct(data)
        self.assertEqual(arr_test.last_num(), 12)

    def test_number_of_prime_numbers(self):
        data = [25667, 8555554, 613344434, 71334565, 126777, 137766, 836544, 6632232]
        arr_test = Struct(data)
        self.assertEqual(arr_test.number_of_prime_numbers(), 1)

    def test_number_of_even_numbers(self):
        data = [4, 8, 9, 23, 12, 16, 19, 456]
        arr_test = Struct(data)
        self.assertEqual(arr_test.number_of_even_numbers(), 5)

    def test_number_of_odd_numbers(self):
        data = [53, 67, 43, 21, 80]
        arr_test = Struct(data)
        self.assertEqual(arr_test.number_of_odd_numbers(), 4)


if __name__ == '__main__':
    unittest.main()
