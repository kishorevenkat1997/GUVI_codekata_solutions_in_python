num = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = [int(y) for y in range(0,len(arr1)+1)]
ans = []
for k , j in zip(arr1,arr2):
    if k == j:
        ans.append(k)
    else:
        pass
if len(ans)==0:
    print('-1')
else:
    ans.sort()
    print(*ans)