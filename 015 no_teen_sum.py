def no_teen_sum(a, b, c):  
 return fix_teen(a)+fix_teen(b)+fix_teen(c)


def fix_teen(value):
 if value in range (13,20):
  if value in range (15,17):
   return value
  else:
   return 0
 else:
  return value
  
print no_teen_sum(2, 1, 14) 
