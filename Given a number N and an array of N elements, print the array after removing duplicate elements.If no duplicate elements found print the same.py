num = int(input())
arr1 = [int(x) for x in input().split()]
ans = set()
for k in arr1:
    ans.add(k)
if num == len(arr1):
    print(*ans)