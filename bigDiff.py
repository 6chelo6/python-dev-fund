def big_diff(nums):
 print getMax(nums)-getMin(nums)
 
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
 
big_diff([10,3,5,6])
