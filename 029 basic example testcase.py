#!/usr/bin/env python

import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		self.seq = range(10)
	
	def test_shuffle(self):
		random.shuffle(self.seq)
		self.seq.sort()
		self.assertEqual(self.seq,rante(10))
	
	
