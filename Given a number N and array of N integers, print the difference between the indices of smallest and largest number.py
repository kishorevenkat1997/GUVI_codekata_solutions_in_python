num = int(input())
arr1 = [int(x) for x in input().split()]
min = min(arr1)
max = max(arr1)
ans = arr1.index(max) - arr1.index(min)
print(abs(ans))