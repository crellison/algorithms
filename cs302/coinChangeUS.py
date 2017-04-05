import sys
from math import floor

def getChange(amount):
  '''
  takes amount in cents and returns object with key:value pairs
  denoting the number of coins of each denomination necessary to
  make change in USD. 

  Runtime: O(1)
  '''
  change = {}
  change[25] = floor(amount/25)
  change[10] = floor((amount%25)/10)
  change[5] = 1 if (amount%25)%10 >= 5 else 0
  change[1] = amount%5
  return change

def numCoins(amount):
  '''
  Uses getChange() to determine the total number of coins needed
  to make change for a given amount.
  '''
  change = getChange(amount)
  num = 0
  for coin in change:
    num += change[coin]
  return num