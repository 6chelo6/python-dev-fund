#!/usr/bin/env python

class Car:
	def __init__(self,brand,color):
		self.brand=brand
		self.color=color
	
	def __eq__(self,other_car):
		print "__eq__ called %r == %r ?" % (self, other_car)
		return self.brand == other_car.brand

my_car = Car("Toyota",'red')
another_car = Car('Toyota',5)

print my_car == another_car

