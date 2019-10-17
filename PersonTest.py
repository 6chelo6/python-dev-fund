#!/usr/bin/env python

import unittest
from Person import *

class PersonTest(unittest.TestCase):
	
	def test_verify_identity(self):
		self.name = "Marcelo"
		self.last_name = "Vargas"
		
		expected_result = "Hello, my name is" + self.name + self.last_name
		
		new_person = Person("Marcelo","Vargas")
		
		salute = new_person.return_salute()
		
		self.assertEqual(salute,expected_result)
	
	def test_updating_name(self):
		
		new_name = "Michael"
		new_person.update_name(new_name)
		my_new_name = new_person.get_name()
		self.assertEqual(my_new_name,new_name)


if __name__ == "__main__":
	unittest.main()
