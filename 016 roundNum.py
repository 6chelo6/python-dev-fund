#!/usr/bin/env python

def round10(num):
 if num%10 >= 5:
  return int(num/10)*10+10
 else:
  return int(num/10)*10

print round10(4)
