num = int(input())
arr = [int(x) for x in input().split()]
first = arr[0] + arr[1] + arr[2]
last = arr[-1] + arr[-2] + arr[-3]
if num == len(arr):
  if first == last:
    print('1')
  else:
    print('0')