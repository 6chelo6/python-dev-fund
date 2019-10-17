#!/usr/bin/env python


def xyz_there(a):
 #return a.count(b)>0 or b.count(a)>0
 
 #return a[len(a)-len(b):].lower() == b[:len(b)].lower() or b[len(b)-len(a):].lower() == a[:len(a)].lower()

  for i in range(len(a)):
   if a[i:i+3].lower() == "xyz" and a[i-1]!='.':
    return True
  else:
   return False

#print end_other('Myabcdfe','abx')
print xyz_there('.xyzMyabc.xyz')
