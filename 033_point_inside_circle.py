#!/usr/bin/env python

import unittest

class Shape:
	def contains(self,other):
		pass
	
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
class Circle(Shape):
	
	def __init__(self,center,radius):
		self.center = center
		self.radius = radius
		
	def contains(self, other):
		distance =  (other.x - self.center.x) ** 2 + (other.y - self.center.y) ** 2
		return distance <= self.radius**2
		
class CircleTest(unittest.TestCase):
	def test_contains_point_returns_true_if_point_is_inside_the_circle(self):
		circle = Circle(Point(0,0),6)
		point = Point (-5,-1)
		self.assertTrue(circle.contains(point))

if __name__ == '__main__':
    unittest.main()
