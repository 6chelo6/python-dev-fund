#!/usr/bin/env python

def string_match(a, b):
 count = 0
 
 
 if len(a) > len(b):
  limit = len(b)
 else:
  limit = len(a)
  
 if len(a)==1 or len(b)==1:
  return 0
 else:
  for i in range(limit-1):
   print i,a[i:i+2],b[i:i+2]
   if a[i:i+2] == b[i:i+2]:
    count += 1
  return count
  
print string_match('abc', 'axc')
