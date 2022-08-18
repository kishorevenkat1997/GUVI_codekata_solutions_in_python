n , k = map(int,input().split())
arr = [int(x) for x in input().split()]
arr.sort()
if n == len(arr):
  if k in arr:
    print('Yes')
  else:
    print("no")
