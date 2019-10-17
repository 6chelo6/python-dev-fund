#!/usr/bin/env python

l = [15, 18, 2, 36, 12, 78, 5, 6, 9]
m = [1, 2, 3, 4, 100]
# print sum(m) / float(len(l))

def getMin(nums):
 minimum = 1000
 for elements in nums:
  if elements<minimum:
   minimum=elements
 return minimum

def getMax(nums):
 maximum = 0
 for elements in nums:
  if elements>maximum:
   maximum=elements
 return maximum

maximum = getMax(m)
minimum = getMin(m)

print sum(m)-(maximum+minimum)
  
