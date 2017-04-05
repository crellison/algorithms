from random import randint

def kSmall(arr,k):
  '''
  finds the kth smallest element from an array of unique elements

  Runtime: O(n*log(n))
  '''
  pIndex = randint(0,len(arr)-1)
  L,R = ([],)*2
  for i in range(0,len(arr)-1):
    if i != pIndex:
      if arr[i] < arr[pIndex]:
        L.append(arr[i])
      if arr[i] > arr[pIndex]:
        R.append(arr[i])
  if len(L) == k-1:
    return arr[pIndex]
  elif len(L) > k-1:
    return kSmall(L,k)
  else:
    return kSmall(R, k-1-len(L))
