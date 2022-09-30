num = int(input())
arr = [int(x) for x in input().split()]
ans = max(arr)
print(arr.index(ans))