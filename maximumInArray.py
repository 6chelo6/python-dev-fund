#!/usr/bin/env python

def max_end3(nums):
  maximum = 0
  array = []
  for element in nums:
   if element > maximum:
    maximum = element
  for i in range (len(nums)):
   array.append(maximum)
  
  return array
