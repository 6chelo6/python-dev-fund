def calculateBothUnits(amountSmall,unitSmall,amountBig,unitBig,goalTemp):
 if (goalTemp % unitSmall == 0 and amountSmall*unitSmall >= goalTemp) and (goalTemp % unitBig == 0 and amountBig*unitBig >= goalTemp):
  return True
 else:
  return False
  
print calculateBothUnits(2,2,2,1,10)


# WRONG CODE, NEEDS IMPROVEMENTS, NEEDS TO WORK
