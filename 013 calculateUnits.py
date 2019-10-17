#!/usr/bin/env python

def calculateUnits(amount,units,goal):
 if goal % units == 0 and amount*units >= goal:
  return True
 else:
  return False

print calculateUnits(6,2,2)
