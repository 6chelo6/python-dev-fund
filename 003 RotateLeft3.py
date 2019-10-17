nums = [1,2,3]
first=nums[0]
print (first)
i=0

for i in range(len(nums)-1):
  nums[i] = nums[i+1]
   
   
nums[len(nums)-1] = first
  
print nums
