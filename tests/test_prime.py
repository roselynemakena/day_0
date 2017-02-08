import unittest
from functions.prime_numbers import is_number_prime

class Prime_Testing(unittest.TestCase):
	#test one
	def test_return_error_when_not_int(self):
		self.assertEqual(is_number_prime("string"), "input parameter is not an int")
	#test two
	def test_is_number_0(self):
		self.assertFalse(is_number_prime(0))
	#test three 	
	def test_is_number_1(self):
		self.assertFalse(is_number_prime(1))
	#test four	
	def test_if_number_is_negative(self):
		self.assertFalse(is_number_prime(-1))
	#test five
	def test_if_number_is_too_large(self):
		self.assertEqual(is_number_prime(10*10),"number is too large")
	#test six
	def test_if_number_is_blank(self):
		self.assertFalse(is_number_prime(""))
	#test seven
	def test_if_number_is_prime(self):
		self.assertTrue(is_number_prime(7))
	#test eight
	def test_if_number_is_not_prime(self):
		self.assertFalse(is_number_prime(9))
	#test nine
	def test_number_of_items_returned_test_one(self):
		self.assertEqual(is_number_prime(range(50), 15))

	#test ten
	def test_number_of_items_returned_test_two(self):
		self.assertequal(is_number_prime(range(10),4))
		
		

if __name__ == '__main__':
	unittest.main()