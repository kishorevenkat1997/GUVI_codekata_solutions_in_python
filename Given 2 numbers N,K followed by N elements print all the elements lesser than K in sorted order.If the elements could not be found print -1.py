n , k = map(int,input().split())
arr1 = [int(x) for x in input().split()]
ans = []
for j in arr1:
    if j < k:
        ans.append(j)
    else:
        pass
if len(ans) == 0:
    print('-1')
else:
    print(*ans)