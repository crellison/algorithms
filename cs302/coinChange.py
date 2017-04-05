# import sys

MAX = 10000

def getChange(amount, denArr):
  '''
  takes a value in cents and an array of denominations, and 
  recursively finds the optimal number of coins to use to make change

  Runtime: O(n*k) k = # of denominations
  '''
  if amount == 0: 
    return 0
  elif amount < 0:
    return MAX
  elif amount in denArr:
    return 1
  else:
    return 1+min([getChange(amount-den,denArr) for den in denArr])


def memoizeCoins(func):
  '''
  Used to memoize coin change
  '''
  memo = {}
  hits = 0
  def helper(amount,denArr):
    if amount not in memo:
      memo[amount] = func(amount,denArr)
    return memo[amount]
  return helper

getChange = memoizeCoins(getChange)

print(getChange(67,[1,2,6,13]))