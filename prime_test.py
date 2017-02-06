import unittest

class Prime_Testing(unittest.TestCase):
	unittest.main()
	def setup(self):
		self.assertTrue(False)
	def raise_error(self):
		raise RunTimeError('test error')
