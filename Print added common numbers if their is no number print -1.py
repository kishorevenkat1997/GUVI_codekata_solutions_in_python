num = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = [int(y) for y in input().split()]
ans = []
for a,b in zip(arr1,arr2):
    if a == b:
        ans.append(a+b)
    else:
        pass
if len(ans) == 0:
    print('-1')
else:
    print(*ans)
