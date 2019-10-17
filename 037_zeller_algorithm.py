#!/usr/bin/env python
import unittest

class ZellerAlgorithm(unittest.TestCase):
	
	def test_return_value(self):
		day=20
		month=2
		year=1982
		weekDay="Saturday" # The correct value is Saturday
		
		weekdays = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
		#print month
		if month == 1:
			A = 11
			year-=1
		elif month == 2:
			A = 12
			year-=1
		else:
			A = month - 2
		
		#month of the year March=1, April=2,...
		
		B = day #day of the month
		
		C = year % 1000 % 100 #year of the century
		
				
		D = (year - C) / 100 #the century
		
		W = (13*A-1)/5
		X = C/4
		Y = D/4
		Z = W + X + Y + B + C - 2 * D

		R = Z % 7 #Sunday=0, Monday=1
		
		self.assertTrue(weekdays[R] == weekDay.lower())
		
	
if __name__ == '__main__':
    unittest.main()
