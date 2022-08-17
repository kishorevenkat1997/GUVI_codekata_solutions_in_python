#Given a number n followed by n numbers short the n number in descending order
num = int(input())
arr = [int(x) for x in input().split()]
arr.sort(reverse=True)
if num == len(arr):
  print(*arr)