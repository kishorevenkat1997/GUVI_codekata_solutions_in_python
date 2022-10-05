num = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = [int(y) for y in input().split()]
ans = []
for k , j in zip(arr1,arr2):
    a = k + j
    ans.append(a)
print(*ans)