import unittest
from functions.prime_numbers import is_number_prime

class Prime_Testing(unittest.TestCase):

	def test_return_error_when_not_int(self):
		self.assertEqual(is_number_prime("blah"), "input parameter is not an int")

	def test_is_number_0(self):
		#should return false
		self.assertFalse(is_number_prime(0))	
	def test_is_number_1(self):
		pass
	def check_if_number_(self):
		pass

if __name__ == '__main__':
	unittest.main()