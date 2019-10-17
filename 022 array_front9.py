#!/usr/bin/env python

def array_front9(nums):
# for i in range(len(nums))
 if nums[:4].count(9)>0:
  return True
 else:
  return False

print array_front9([1, 2, 9, 4, 5])
