#!/usr/bin/env python


def end_other(a, b):
 #return a.count(b)>0 or b.count(a)>0
 
 #return a[len(a)-len(b):].lower() == b[:len(b)].lower() or b[len(b)-len(a):].lower() == a[:len(a)].lower()

 if len(a)>len(b):
  for i in range(len(a)-len(b)+1):
   #print "a[",i,",",i+len(b)-1,"],b[",0,",",len(b),"]"," >> [",a[i:i+len(b)].lower(),"==",b[0:len(b)].lower(),"]"
   if a[i:i+len(b)].lower() == b[0:len(b)].lower():
    return True
  else:
   return False
 else:
  for i in range(len(b)-len(a)+1):
   
   if b[i:i+len(a)].lower() == a[0:len(a)].lower():
    return True
  else:
   return False

#print end_other('Myabcdfe','abx')
print end_other('bc','Myabcx')
