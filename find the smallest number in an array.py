num = int(input())
arr = [int(x) for x in input().split()]
if num == len(arr):
    print(min(arr))