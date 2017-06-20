import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
	"""Tests for 'primes.py'."""

	def test_is_five_prime(self):
		"""Is five successively determined to be prime?"""
		self.assertTrue(is_prime(5), msg='Five is prime!')

	def test_is_four_prime(self):
		"""Is four correctly determined not to be prime?"""
		self.assertFalse(is_prime(4), msg='Four is not prime!')

	def test_is_zero_prime(self):
		"""Is zero correctly determined not to be prime?"""
		self.assertFalse(is_prime(0), msg='Zero is not prime!')

	def test_is_one_thousand_prime(self):
		"""Is 1,000 correctly determined not to be prime?"""
		self.assertFalse(is_prime(1000), msg='1,000 is not prime!')

	def test_negative_number(self):
		"""Is a negative number correctly determined not to be prime?"""
		for index in range(-1, -10, -1):
			self.assertFalse(is_prime(index), msg='{} should not be determined to be prime!'.format(index))

if __name__ == '__main__':
	unittest.main()