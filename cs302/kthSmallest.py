from random import randint

def kSmall(arr,k):
  '''
  finds the kth smallest element from an array of unique integers/floats

  Runtime: O(n*log(n))
  '''
  pIndex = randint(0,len(arr)-1)
  L,R = ([],)*2
  # partition step
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

def kSmallSmart(arr,k):
  '''
  finds the kth smallest elt from an array of integers/floats

  Runtime: O(n)
  '''
  pivot = arr[randint(0,len(arr)-1)]
  L,R = ([],)*2
  pivotCount = 0
  # partition step
  for elt in arr:
    if elt == pivot:
      pivotCount += 1
    elif elt < pivot:
      L.append(elt)
    else:
      R.append(elt)

  if len(L) + pivotCount > k:
    return pivot
  elif len(L) > k:
    return kSmall(L,k)
  else:
    k = k - len(L) -pivotCount
    return kSmall(R, k)