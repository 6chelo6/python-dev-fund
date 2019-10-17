#!/usr/bin/env python

def sum67(nums):
 suma = 0
 i = 0
 flag = False
 while i < len(nums):
  if flag:
   if nums[i]==7:
    flag = False
    i = i+1
   else:
    i = i + 1
  else:
   if (nums[i]==6):
    flag = True
    i = i + 1
   else:
    suma = suma + nums[i]
    i = i + 1
 print suma
   
 
sum67([1, 2, 2, 6, 99, 99, 7])
