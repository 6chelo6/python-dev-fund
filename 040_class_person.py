#!/usr/bin/env python

class Person():
	def __init__(self,name,last_name):
		self.name = name
		self.last_name = last_name
	
	def return_salute(name,last_name):
		return "Hello, my name is" + name + last_name
	
