n , m = map(int,input().split())
arr = [int(x) for x in input().split()]
arr_1 = []
if n == len(arr):
  for k in arr:
    if k != m:
      arr_1.append(k)
    else:
      pass
if len(arr) == len(arr_1):
  print("-1")
else:
  print(*arr_1)