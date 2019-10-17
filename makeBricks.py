#!/usr/bin/env python

def neededAmountBigs(goal, unitBig):
 return int(goal/unitBig)

def calculateUnits(amount,units,goalTemp):
 if goalTemp % units == 0 and amount*units >= goalTemp:
  return True
 else:
  return False

def make_bricks(small, big, goal):
 smallUnit = 2
 bigUnit = 5
 
 currentSmall = small*smallUnit
 currentBig = big*bigUnit

 
 if calculateUnits(big,bigUnit,goal):
  return True
 else:
  if currentBig > goal:
   remainingUnits = goal-neededAmountBigs(goal,bigUnit)*5
   if calculateUnits(small,smallUnit,remainingUnits):
    return True
   else:
    return False
  else: 
   remainingUnits = goal - currentBig   
   if calculateUnits(small,smallUnit,remainingUnits):
    return True
    
   else:
    return False
      
     
 

print make_bricks(9,1,10)
