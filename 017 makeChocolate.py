#!/usr/bin/env python

def calculateUnits(amount,units,goalTemp):
 if goalTemp % units == 0 and amount*units >= goalTemp:
  return True
 else:
  return False

def neededAmountBigs(goal, unitBig):
 return int(goal/unitBig)

def make_chocolate(small, big, goal):
 smallUnit = 1
 bigUnit = 5
 
 currentSmall = small*smallUnit
 currentBig = big*bigUnit
 
 neededBigs = neededAmountBigs(goal,bigUnit)
 
 if calculateUnits(big,bigUnit,goal):
  return 0
 else:
  if currentBig > goal:
   remainingUnits = goal-neededAmountBigs(goal,bigUnit)*5
   if calculateUnits(small,smallUnit,remainingUnits):
    return remainingUnits
   else:
    return -1
  else: 
   remainingUnits = goal - currentBig   
   if calculateUnits(small,smallUnit,remainingUnits):
    return remainingUnits
    
   else:
    return -1
  
   

print make_chocolate(6,2,7)
