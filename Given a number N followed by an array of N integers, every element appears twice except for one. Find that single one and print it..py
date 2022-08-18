#Given a number N followed by an array of N integers, every element appears twice except for one. Find that single one and print it.
num = int(input())
arr = [int(x) for x in input().split()]
r = []
r1 = []
nr = []
for k in arr:
  if k not in r :
    r.append(k)
  elif k in r:
    r1.append(k)
for j in arr:
  if num == len(arr):
    if j not in r1:
      nr.append(j)
print(*nr)