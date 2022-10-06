n , k = map(int,input().split())
arr1 = [int(x) for x in input().split()]
ans = []
for j in arr1:
    if j == k:
        continue
    else:
        ans.append(j)
if len(ans) == 0:
    print('empty')
else:
    print(*ans)