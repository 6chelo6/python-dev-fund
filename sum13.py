#!/usr/bin/env python
nums = [13, 1, 2, 13, 2, 1, 13]
suma = 0
i = 0

while i < len(nums):
		if nums[i]==13:
			i = i + 2 
		else:
			suma = suma + nums[i]
			i = i + 1
print suma
