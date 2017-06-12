# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


class SimpleTest(TestCase):
	"""docstring for SimpleTest"""
	def test_basic_addition(self):
		"""
		Test that 1 + 1 always equsls 2.
		"""
		self.assertEqual(1+1,2)
		