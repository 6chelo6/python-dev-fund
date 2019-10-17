#!/usr/bin/env python

def has22(nums):

 i = 0
 flag = False
 
 while i < len(nums):
  if flag:
   if nums[i]==2:
	print "True"
	break
   else:
    print "nice try"
    flag = False
    i = i + 1
  else:     
   if nums[i]==2:
    flag = True
    i = i + 1
   else:
    i = i + 1
 else:
  print "False"
 
has22([4, 2, 4, 2, 2, 5])
