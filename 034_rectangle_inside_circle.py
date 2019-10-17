#!/usr/bin/env python

import unittest

class Shape:
	def contains(self,other):
		pass
	
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Rectangle(Shape):
	def __init__(self, top_left, width, height):
		self.top_left = top_left
		self.width = width
		self.height = height
	@property
	def top_right(self):
		return Point(self.top_left.x+self.width, self.top_left.y)
	
	@property
	def bottom_left(self):
		return Point(self.top_left.x, self.top_left.y+self.height)
	
	@property
	def bottom_right(self):
		return Point(self.top_left.x+self.width, self.top_left.y+self.height)
	
class Circle(Shape):
	
	def __init__(self,center,radius):
		self.center = center
		self.radius = radius
		
	def contains(self, other):
		distance1 =  (other.top_left.x - self.center.x) ** 2 + (other.top_left.y - self.center.y) ** 2
		distance2 =  (other.top_right.x - self.center.x) ** 2 + (other.top_right.y - self.center.y) ** 2
		distance3 =  (other.bottom_left.x - self.center.x) ** 2 + (other.bottom_left.y - self.center.y) ** 2
		distance4 =  (other.bottom_right.x - self.center.x) ** 2 + (other.bottom_right.y - self.center.y) ** 2
		return distance1 <= self.radius ** 2 and distance2 <= self.radius ** 2 and distance3 <= self.radius ** 2 and distance4 <= self.radius ** 2
		
class CircleTest(unittest.TestCase):
	def test_contains_point_returns_true_if_point_is_inside_the_circle(self):
		circle = Circle(Point(0,0),6)
		point = Point(2,2)
		rectangle = Rectangle(point,1,1)
		self.assertTrue(circle.contains(rectangle))

if __name__ == '__main__':
    unittest.main()
