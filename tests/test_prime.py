import unittest
from functions.prime_numbers import is_number_prime

class Prime_Testing(unittest.TestCase):

	def test_return_error_when_not_int(self):
		self.assertEqual(is_number_prime("string"), "input parameter is not an int")
	def test_is_number_0(self):
		self.assertFalse(is_number_prime(0))	
	def test_is_number_1(self):
		self.assertFalse(is_number_prime(1))	
	def test_if_number_is_negative(self):
		self.assertFalse(is_number_prime(-1))
	def test_if_number_is_too_large(self):
		self.assertEqual(is_number_prime(10*10),"number is too large")
		

if __name__ == '__main__':
	unittest.main()