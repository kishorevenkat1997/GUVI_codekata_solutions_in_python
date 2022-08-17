num = int(input())
arr = [int(x) for x in input().split()]
arr1 = [int(y) for y in input().split()]
add = []
for z in range(len(arr)):
  add.append(arr[z] + arr1[z])
if len(arr) == num and len(arr1) == num:
  print(*add)