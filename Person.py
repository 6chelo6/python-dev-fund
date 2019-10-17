#!/usr/bin/env python

class Person():
	def __init__(self,name,last_name):
		self.name = name
		self.last_name = last_name
	
	def return_salute(self):
		return "Hello, my name is" + self.name + self.last_name
	
	def update_name(new_name):
		self.name = new_name
		return self.name

	def get_name(self):
		return self.name