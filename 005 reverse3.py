#!/usr/bin/env python
nums = [8,9,10]
posicion = len(nums)

# print posicion
array = []

for i in range (len(nums)):
 #print nums[i]
 array.append(nums[posicion-1])
 posicion = posicion - 1
print array
