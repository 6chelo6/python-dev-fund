#!/usr/bin/env python

import unittest
from Person import *

class PersonTest(unittest.TestCase):
	
	def test_verify_identity(self):
		self.name = "Marcelo"
		self.last_name = "Vargas"
		
		expected_result = "Hello, my name is" + name + last_name
		
		new_person = Person("Marcelo","Vargas")
		
		salute = new_person.return_salute()
		
		self.assertEqual(salute,expected_result,"Mensaje personalizado")
